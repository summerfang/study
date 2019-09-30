function add(x,y,f) {
    return f(x) + f(y);
}

var a = add(10,20, Math.sqrt);
console.log("The answer is " + a);

var arr = [1,2,3,4,5,6];

function test(params) {
    return params*params;
}

var result = arr.map(test);

console.log(result);

var sumofresult = result.reduce(function f(p1,p2) {
    return p1+p2;
});

console.log(sumofresult);

var r1 = arr.filter(function f1(params) {
    if(params%2 == 0)
        return true;
    else
        return false;    
})

console.log(r1);

r2 = r1.sort(function desc(p1,p2) {
    if(p1>p2)
        return -1;
    else if (p1==p2)
        return 0;
    else
        return 1;
});

console.log(r2);