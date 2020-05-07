import _ from "lodash";
import "./style.css";
import Icon from "./logo.svg";
import Data from "./data.xml";
import printMe from "./print.js";

function component(){
    const element = document.createElement("div");
    element.innerHTML = _.join(["Hello", "World!"],"");
    element.classList.add("hello");

    const myIcon = new Image();
    myIcon.src = Icon;

    element.appendChild(myIcon);

    const btn = document.createElement("button");
    btn.innerHTML = "Click me and chek the console!";
    btn.onclick = printMe;
    element.appendChild(btn);
    
    console.log(Data);
    return element;
}

document.body.appendChild(component());

