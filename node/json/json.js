var fs = require('fs');
var http = require('http');
const { endianness } = require('os');

http.createServer(function(req, res){
    fs.readFile('m.json', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});

        var obj = JSON.parse(data);
        res.write(obj.v1.meeting_id);

        for(i = 0; i < obj.v1.rosters.length; i++) {
            res.write(r.name) + "<br>";
        }
        res.end();
    
    });
}).listen(8000)