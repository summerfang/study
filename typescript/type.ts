
//Any type 
let any_object: any;

any_object = 100;
console.log(any_object);
any_object = "Hello";
console.log(any_object);


//Number
let binary_number: number = 0b1111;
console.log(binary_number);
let octonary_number: number = 0o7777;
console.log(octonary_number);
let decimal_number: number = 9999;
console.log(decimal_number);
let hexadecimal_number: number = 0xffff;
console.log(hexadecimal_number);


//String
let str: string = "Hello World";
console.log(str);

//Array
let arr: number[] = [1,2];
console.log(arr[0]);

let arr_gen: Array<number> = [10,100]
console.log(arr_gen[0])


//boolean
let b: boolean = true

if(b)
    console.log("I am true!");


//tulp
let t: [number, string, number] = [10, "hello", 100];
console.log(t[1])

//enumerator

enum colors {Red, Yello, Green}
let c1: colors = colors.Red
console.log(c1)


//void
function fn() : void {
    console.log("Do nothing");
}


//null
let a: any = null
console.log(typeof(a));

//undefined

if(b == undefined)
    console.log("b is undefined")

//never
let x: never;
let y: number;

x = (()=>{
    throw new Error('exception')
})();

y = (()=>{throw Error("Mistake!")})();

function never_fun(message:string): never {
    throw new Error(message + ' is a mistake!');
}

never_fun("What");

function lool_endless(): never {
    while(true){}
}
