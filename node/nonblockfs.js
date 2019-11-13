var file = require('fs');

file.readFile('input.txt', function(err, data){
    if (err)
        return console.error(err);
    else
        console.log(data.toString());
});

console.log('The progam is end!');