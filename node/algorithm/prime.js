function isPrime(num){
    //Negative, 0, 1 is not a prime number
    if(num <= 1)
        return false;

    b = true; //Assume num is a prime
    for(i=2; i<num; i++) {
        if((num%i) == 0 ){ //If any i could be devided, it is not a prime number
            b = false;
            break;
        }
    }

    return b;
}

console.log("-1 is a prime number is " + isPrime(-1));
console.log("0 is a prime number is " + isPrime(0));
console.log("1 is a prime number is " + isPrime(1));
console.log("2 is a prime number is " + isPrime(2));
console.log("19 is a prime number is " + isPrime(19));