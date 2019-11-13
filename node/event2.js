var event = require('events');

var anEvent = new event.EventEmitter();

var EventHandler1 = function(arg1, arg2){
    if(arg1){
        console.log(arg1.stack);
        return;
    }
    else
        console.log('This is event handler 1', arg1, arg2);
}

var EventHandler2 = function(arg1, arg2){
    if(arg1){
        console.log(arg1.stack);
        return;
    }
    else
        console.log('This is event handler 2', arg1, arg2);
}

anEvent.on('Event1', EventHandler1);
anEvent.emit('Event1', 'Say', 'Event 1');

anEvent.addListener('Event1', EventHandler2);
anEvent.emit('Event1', 'Hello', 'World!');

anEvent.removeListener('Event1', EventHandler2);
console.log('Event Handler 2 is removed');

anEvent.emit('Event1', 'Second', 'Event');
anEvent.emit('error');