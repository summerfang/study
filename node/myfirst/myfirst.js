var dt = require("./myfirstmodule");
var http = require("http");

http.createServer(function(req, res) {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.write("The date and time are currently: " + dt.myDateTime());
    res.write(req.url);
    res.end();
}).listen(8008);