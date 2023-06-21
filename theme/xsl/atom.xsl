<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"
                xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <title><xsl:value-of select="/atom:feed/atom:title"/> Atom Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
        <style type="text/css">
          * { box-sizing: border-box; }
          img { max-width: 100%; }
          body { --gap: 5vw; margin: 0; font-family: system-ui; line-height: 1.7; }
          h1,h2,h3 { margin-block-start: 0; margin-block-end: 0; }
          .pb-5 { padding-bottom: calc(var(--gap) / 8); }
          .intro-container { color: #676767; }
          .container, .intro-container {
            display: grid;
            gap: calc(var(--gap) / 2);
            // max-width: 46rem;
            width: 95%;
            margin: auto;
          }
          .intro {
            background-color: rgb(251,192,45);
            margin-block-end: calc(var(--gap) / 2);
            padding-block: calc(var(--gap) / 4);
          }
          .intro .intro-container {
            gap: 1rem;
            grid-template-columns:  4fr 2fr;
            align-items: top;
          }
          @media (min-width: 40rem) {
            .intro .container {
              grid-template-columns:  4fr 1fr;
              align-items: center;
            }
          }
          .recent {
            padding-block-end: var(--gap);
          }
          img {
            height: auto;
            width: 10rem;
          }
          body {
            background-color: #222222;
          }
          .container {
            color: #eeeeee;
          }
          small {
            font-size: 12px;
            letter-spacing: 0;
            margin: 0 0 16px;
            color: #eeeeee;
          }
          a:hover {
            color: #424242;
          }
          h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            text-decoration: none;
          }
          a {
            -webkit-transition: color .3s ease 0s;
            transition: color .3s ease 0s;
            color: #ffd740;
            font-weight: 500;
            color: #ffd740;
          }
          h2 {
            font-size: 36px;
            line-height: 48px;
          }
          h3 {
            font-size: 30px;
            line-height: 40px
          }
        </style>
      </head>
      <body>
        <nav class="intro">
          <div class="intro-container">
            <div>
              <p><strong>You found me!</strong> This is my Atom feed. You can <strong>Subscribe</strong> by copy-pasting the URL into your RSS feed reader.</p>
            </div>
            <img src="/theme/images/error.png"  />
          </div>
        </nav>
        <div class="container">
          <header>
            <h1><xsl:value-of select="/atom:feed/atom:title"/></h1>
            <p><xsl:value-of select="/atom:feed/atom:description"/></p>
            <a class="head_link" target="_blank">
              <xsl:attribute name="href">
                <xsl:value-of select="/atom:feed/atom:link/@href"/>
              </xsl:attribute>
              Visit Website &#x2192;
            </a>
          </header>
          <section class="recent">
            <h2>Recent Items</h2>
            <xsl:for-each select="/atom:feed/atom:entry">
              <div class="pb-5">
                <h3>
                  <a target="_blank">
                    <xsl:attribute name="href">
                      <xsl:value-of select="atom:link/@href"/>
                    </xsl:attribute>
                    <xsl:value-of select="atom:title"/>
                  </a>
                </h3>
                <small class="meta">
                  Published: <xsl:value-of select="atom:published" />
                </small>
              </div>
            </xsl:for-each>
          </section>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
