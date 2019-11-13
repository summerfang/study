var express = require('express');
var app = express();

app.use('/public', express.static('public'));

app.get('/index.htm', function(req, res){
    res.sendFile(__dirname + "/" + "index.htm");
})

app.get('/process_get', function(req, res){
    var response = {
        "first_name" : req.query.first_name,
        "last_name": req.query.last_name
    };

    console.log(response);
    res.end(JSON.stringify(response));
})

var server = app.listen(8091, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log("Access http;//%s:%s", host, port);
})