function add(x,y,f){
    return f(x) + f(y);
}


function f(x) {
    return x;
}

console.log("Add="+add(1,2,f));
console.log("Square="+add(1,2,Math.sqrt));