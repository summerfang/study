var http = require('http');
var fs = require('fs');
var url = require('url');

http.createServer((req, res) => {
    var pathname = url.parse(req.url).pathname;
    console.log("Req is " + pathname);

    fs.readFile(pathname.substr(1), (err, data)=>{
        if(err) {
            console.log(err);
            res.writeHead(404, {'Content-Type' : 'text/html'});
        } else {
            res.writeHead(200, {'ContentType': 'text/html'});
            res.write(data.toString());
        }
        res.write("Hello World1");
        res.end();
    });

}).listen(8080);

console.log("Listen 8080");