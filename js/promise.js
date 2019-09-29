var isSuccess = true;

function s(){
    console.log("Success!");
}

function f(){
    console.log("fail");
}

function w(s,f){
    setTimeout(()=>{}, 1000);

    if(isSuccess) {
        s();
    } else{
        f();
    }
}

var a = new Promise(w);
a.then(()=>{
    console.log("This come from success!");
}).catch(()=>{
    console.log("This fails");
});

