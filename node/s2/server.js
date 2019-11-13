var express = require('express');

var app = express();

app.get('/', function(req, res){
    res.send('Hello Get');
    console.log('Hello Get it');
});

app.post('/', function(req, res){
    res.send('Hello Post');
    console.log('Hello Post');
});

app.get('/del_user', function(req, res) {
    res.send('Delete user!');
    console.log('Dele user');
});

app.get('/list_user', function(req, res) {
    console.log('list user')
    res.send('List user');
});

app.get('/ab*cd', function(req, res) {
    console.log('/ab*cd request');
    res.send('/ab*cd');
});

var server = app.listen(8090, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log("App access http://%s:%s", host, port);
});