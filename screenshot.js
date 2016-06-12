var page = require('webpage').create(),
    system = require('system');
address = system.args[1];
output = system.args[2];
page.viewportSize = { width: 1920, height: 1080 };
page.clipRect = { top: 0, left: 0, width: 1920, height: 1080 };
page.open(address, function() {
  page.evaluate(function() {
    document.body.bgColor = '#FFFFFF';
  });
  page.render(output);
  phantom.exit();
});
