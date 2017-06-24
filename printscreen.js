var page = require('webpage').create(),
    system = require('system');
address = system.args[1];
output = system.args[2];
page.viewportSize = { width: 1920, height: 1080 };
page.onResourceRequested = function(requestData, request) {
    if ((/https:\/\/.+?\.js/gi).test(requestData['url'])) {
        console.log('The url of the request is matching. Aborting: ' + requestData['url']);
        request.abort();
    }
};
page.open(address, function() {
  page.evaluate(function() {
    document.body.bgColor = '#FAFAFA';
  });
  page.render(output);
  phantom.exit();
});
