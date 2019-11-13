var http = require('http');
var f = require('fs');
var event = require('events');
var emitter = new event.EventEmitter();
var i = 0;

emitter.on('Connection', (arg1, arg2) => {
    console.log("Event Connected!" + (i ++ ) + arg1 + arg2);
})

var str = '';


var s = http.createServer(
    (req, res) => {
        f.readFile("input.txt", function(err, data) {
            if(err){
                console.log(err.message);
            } else {
                str = data.toString();
                console.log(str);
                }
        
        });        
        var data = f.readFileSync('input.txt');

        res.writeHead(200, {'content-type': 'text/plain'});
        res.write("sync"+data);
        res.write("asyn" +str);
        res.end('Hello World!');
        emitter.emit('Connection', 'data:'+data, 'str='+str);
    }
).listen(8282);

console.log('Server is running at 8282.');