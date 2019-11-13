var event = require('events');

var aEE = new event.EventEmitter();

aEE.on('TestEvent', function(){
    console.log('Test Event happened');
});

setTimeout(() => {
    aEE.emit('TestEvent');
}, 5000);
