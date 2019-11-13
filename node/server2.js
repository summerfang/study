var http = require('http');

http.createServer(function(req, res){
  res.writeHead(200, {'ContentType':'plain/text'});
  res.end('Hello World!');
}).listen(8800);
