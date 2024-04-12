var m1 = function(){

}

var m2 = function test(){

}

! function(){
    console.log("Hello");
}();

var module = (function(){
    _count: 0;
    var f1 = function(){
        _count = 1;
        return _count; 
    }
    return {f1:f1};
})()


console.log(module.f1());

(function(){
    console.log("From style 1");
})();

(function f1(){
    console.log("From style f1");
})();

(function(){
    console.log("From sytle 2");
}());
(function f2(){
    console.log("From sytle f2");
}());

var str = (function test(){
     return ("From anounymous");
})();

console.log(a=str);

