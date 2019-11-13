var file = require('fs');

var data = file.readFileSync('input.txt');

console.log(data.toString());
