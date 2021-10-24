Playing with Cloudflare Workers: Injecting CSP nonces in to responses
#####################################################################
:date: 2021-10-24 12:00
:author: kura
:category: misc
:tags: cloudflare http content-security-policy csp
:slug: playing-with-cloudflare-workers-injecting-csp-nonce
:related_posts: playing-with-cloudflare-workers-adding-random-pokemon-header

.. contents::
    :backlinks: none

``Content-Security-Policy`` (CSP) is an HTTP header returned by servers that
gives the client some information on where resources can be loaded. For
example setting ``script-src 'self'`` in the CSP tells the client that it should
only load script resources from the current origin. ``'self'`` for this blog post
would mean ``https://kura.gg``.

To make loading those resources more secure you can use hashes or nonces within
the CSP that the client can verify. Below I will show how I inject CSP nonces
using Cloudflare Workers in to responses from my origin.

Security considerations
=======================

**Think of this as an academic exercise rather than something you should do.**

This article will only explain how I inject the nonces in to responses from the
origin. This isn't really secure given the method I use to do this is pretty dumb
-- it just adds a generated nonce to ``<script>`` and ``<link rel="stylesheet>"``
HTML tags, so an attacker could just modify the origin and add a resource to the
HTML and this worker configuration would blindly add a nonce to it.

How it works
============

When a new request comes in, the worker will generate a nonce. The content
is then requested from the origin and the worker modifies the origin response;
injecting the nonce in to ``<script>`` and ``<link rel="stylesheet>"`` HTML tags
and adding the CSP headers which also includes the nonce.

The code
========

This is the full set of worker could to add nonces to responses, there are a few
comments within the code that give an idea of what each part does.

.. code:: javascript

    class AttributeRewriter {
      constructor(nonce, tag_name) {
        this.nonce = nonce
        this.tag_name = tag_name
      }
      
      // There is definitely a cleaner way to do this but JS isn't my
      // strong suit and I didn't want the nonce applied to every <link>
      // tag.
      element(element) {
        if (this.tag_name == "link") {
          const attribute = element.getAttribute("rel")
          if (attribute && attribute == "stylesheet") {
            element.setAttribute("nonce", this.nonce)
          }
        } else {
          element.setAttribute("nonce", this.nonce)
        }
      }
    }

    async function handle_req(req) {
      // Generate the nonce and create a CSP to be added to headers
      // later.
      const nonce = btoa(crypto.getRandomValues(new Uint32Array(2)))
      // This policy only allows using scripts, styles, images and fonts
      // resources from the current origin.
      const content_security_policy = [
        "default-src 'self';",
        "script-src 'self' 'nonce-" + nonce + ";",
        "style-src 'self' 'nonce-" + nonce + ";",
        "img-src 'self';",
        "font-src 'self';",
        "connect-src 'none';",
        "media-src 'none';",
        "object-src 'none';",
        "child-src 'none';",
        "frame-ancestors 'none';",
        "form-action 'none';",
        "upgrade-insecure-requests;",
        "manifest-src 'none';",
        "require-trusted-types-for 'script';"
      ].join(" ")
     
      // Make the request upstream and create a mutable copy of the
      // response headers.
      // const res = await fetch(req.url)
      const res = await fetch("https://kura.gg/")
      let res_headers = new Headers(res.headers)

      // Set up the rewriter, passing the nonce to it for adding to
      // the configured elements.
      const rewriter = new HTMLRewriter()
        .on("script", new AttributeRewriter(nonce, "script"))
        .on("link", new AttributeRewriter(nonce, "link"))

      // Only run the rewriter on HTML content.
      const content_type = res.headers.get("Content-Type")
      let new_res = res
      if (content_type.startsWith("text/html")) {
        new_res = rewriter.transform(res)
      }
      
      // Set the CSP header.
      res_headers.set("Content-Security-Policy", content_security_policy)

      // Return the (possibly modified) body and modified headers.
      return new Response(new_res.body, {
        status: res.status,
        statusText: res.statusText,
        headers: res_headers
      })
    }

    addEventListener('fetch', event => {
      event.respondWith(handle_req(event.request))
    })
