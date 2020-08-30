// Normal viarable
var num: number = 100;
var str1: string = "Hello World";


// Type assert
var n1: number = <number> <any> "1"
console.log(typeof(n1));

// Type detecting
var t1 = 1
console.log(typeof(t1))


// Viarable scope
class VClass {
    num_v1 = 100;
    static s_v2 = 1000;

    f1(p1: number): void {
        
        var local_p1 = p1;
    }

    static s_value : string = "World! Hello";
};

console.log(VClass.s_value)

let v: VClass = new VClass();

v.num_v1 = v.num_v1 + 1;
console.log(v.num_v1)