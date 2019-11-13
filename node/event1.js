var event = require('events');

var ev = new event.EventEmitter();

var eventHandler = function(){
    console.log('I am in eventHandler');
    ev.emit('Test');
}

ev.on('Test', function(){
    console.log('I am in Test');
})

ev.on('Doit', eventHandler);

ev.emit('Doit');