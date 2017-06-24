var disqus_config = function () {
  this.page.url = "https://kura.io" + window.location.pathname;
  this.page.identifier = window.location.pathname;
};

if (document.getElementById('disqus_thread')) {
  (function() {
    var d = document, s = d.createElement('script');
        s.src = '//syslogtv.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
  })();
}
