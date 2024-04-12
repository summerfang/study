function callback(){
    console.log('Done');
}

console.log('Before settimeout()');

setTimeout(callback, 1000);
console.log('After settimeout()');

function test(resolve, reject) {
    var timeOut = Math.random() * 2;
    setTimeout(()=>{
        if(timeOut > 1)
            resolve('>1');
        else
            reject('<1');
    }, 1000);
};

var p1 = new Promise(test);
p1.then(function(result){
    console.log(result+':success');
}).catch(function(result){
    console.log(result+':fail');
})