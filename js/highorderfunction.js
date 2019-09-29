function add(x,y,f) {
    return f(x) + f(y);
}

var a = add(10,20, Math.sqrt);
console.log("The answer is " + a);