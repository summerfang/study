var module1 = function(){
    var sum = 0;
    for(i=0; i<10; i++)
        sum = sum +i;

    return sum;
};

console.log(module1())

var module2 = {
    name = function(){},
    Age = function(){}
}

console.log(module2.Age())
var module3 = new Object({
    
});

var module4 = new Object({
    _count: 0,
    f1: function(){

    },
    f2: function(){

    }
});

module4._count = 1;
module4.f1();

var module5 = new {
    _count: 0,
    f1: function(){

    }
}

