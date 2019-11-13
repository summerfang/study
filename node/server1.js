var http = require('http');

http.createServer(function (req, res){
    res.writeHead(200, {'Content-Type':'text/plain'});
    res.end('Hello World!');
    console.log('This is example is difference!');
    console.log('The result is displayed in the Command Line Interface!')
}).listen(8889);