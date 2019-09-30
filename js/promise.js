var isSuccess = false;

// function s(){
//     console.log("Success!");
// }

// function f(){
//     console.log("fail");
// }

function w(resolve, reject){
    setTimeout(()=>{}, 1000);

    if(isSuccess) {
        resolve("Ok");
    } else{
        reject("Fail");
    }
}

var a = new Promise(w);
a.then(()=>{
    console.log("This come from success!");
}).catch(()=>{
    console.log("This fails");
});

