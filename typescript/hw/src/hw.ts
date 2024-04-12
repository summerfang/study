import fun1, { fun2, fun3 } from "./sub/lib"
import { XMLHttpRequest } from 'xmlhttprequest-ts'

let msg = "Hello World!";
console.log(msg)

let abcd = "God";
console.log(abcd);

console.log(fun1())
console.log(fun2())
console.log(fun3())


let promise1 = new Promise((resolve, reject)=>{
    let msg = "Hello!";

    resolve(msg);
    reject(msg)
});

promise1.then(
    (value)=>{console.log("this is from resolve function" + value)}, 
    (value)=>(console.log("This is from rejct" + msg))
);

// Using call back to implement a feature which retrieve the content of a web site.

function showContent(msg: string) {
    console.log(msg);
}

function retrieveWeb(url : string, callBackFunc : (s: string)=>void) {

    let web = new XMLHttpRequest();
    web.open('GET', url, true);

    web.onreadystatechange  = function () {
        if (web.readyState === 4 && web.status === 200) {
            callBackFunc(web.responseText);
        } else {
            callBackFunc("Error=" + web.status);
        }
    }
    web.send()

}

retrieveWeb('https://www.google.com', showContent)


// Use promise

let webPromise = new Promise((resolve, reject)=>{
    let web = new XMLHttpRequest();
    web.open('GET', 'https://www.google.come',true);
    web.onreadystatechange  = function() {
        if (web.readyState === 4 && web.status === 200) {
            resolve(web.responseText);
        } else {
            reject("Error=" + web.status); 
        }
    };
    web.send();
})

webPromise.then(
    (value) => {showContent(value as string);},
    (value) => {showContent(value as string);},
)

// Using axios for promise

import axios from 'axios';



let webPromise2 = new Promise((resolve, reject) => {
    axios.get('https://www.google.com').then((res) => {
        resolve(res.data);
    })
        .catch((error) => {

            reject(error.message)
        });
})

webPromise2.then(
    (value) => { showContent(value as string); },
    (value) => { showContent(value as string); },
)

// Using fetch
