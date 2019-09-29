import { isPrime } from './prime.js';
import PrimeClass from './prime.class.js';

// onePrime = new Prime(); //This line has syntax error.

console.log("-1 is a prime number is " + isPrime(-1));
console.log("0 is a prime number is " + isPrime(0));
console.log("1 is a prime number is " + isPrime(1));
console.log("2 is a prime number is " + isPrime(2));
console.log("19 is a prime number is " + isPrime(19));

var aPrime = new PrimeClass();

console.log("-1 is a prime number is " + aPrime.isPrime(-1));
console.log("0 is a prime number is " + aPrime.isPrime(0));
console.log("1 is a prime number is " + aPrime.isPrime(1));
console.log("2 is a prime number is " + aPrime.isPrime(2));
console.log("19 is a prime number is " + aPrime.isPrime(19));
