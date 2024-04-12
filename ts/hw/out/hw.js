"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const lib_1 = __importStar(require("./sub/lib"));
const xmlhttprequest_ts_1 = require("xmlhttprequest-ts");
let msg = "Hello World!";
console.log(msg);
let abcd = "God";
console.log(abcd);
console.log((0, lib_1.default)());
console.log((0, lib_1.fun2)());
console.log((0, lib_1.fun3)());
let promise1 = new Promise((resolve, reject) => {
    let msg = "Hello!";
    resolve(msg);
    reject(msg);
});
promise1.then((value) => { console.log("this is from resolve function" + value); }, (value) => (console.log("This is from rejct" + msg)));
// Using call back to implement a feature which retrieve the content of a web site.
function showContent(msg) {
    console.log(msg);
}
function retrieveWeb(url, callBackFunc) {
    let web = new xmlhttprequest_ts_1.XMLHttpRequest();
    web.open('GET', url, true);
    web.onreadystatechange = function () {
        if (web.readyState === 4 && web.status === 200) {
            callBackFunc(web.responseText);
        }
        else {
            callBackFunc("Error=" + web.status);
        }
    };
    web.send();
}
retrieveWeb('https://www.google.com', showContent);
// Use promise
let webPromise = new Promise((resolve, reject) => {
    let web = new xmlhttprequest_ts_1.XMLHttpRequest();
    web.open('GET', 'https://www.google.come', true);
    web.onreadystatechange = function () {
        if (web.readyState === 4 && web.status === 200) {
            resolve(web.responseText);
        }
        else {
            reject("Error=" + web.status);
        }
    };
    web.send();
});
webPromise.then((value) => { showContent(value); }, (value) => { showContent(value); });
// Using axios for promise
const axios_1 = __importDefault(require("axios"));
let webPromise2 = new Promise((resolve, reject) => {
    axios_1.default.get('https://www.google.com').then((res) => {
        resolve(res.data);
    })
        .catch((error) => {
        reject(error.message);
    });
});
webPromise2.then((value) => { showContent(value); }, (value) => { showContent(value); });
// Using fetch
//# sourceMappingURL=hw.js.map