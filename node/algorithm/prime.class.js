module.exports = class Prime {
  isPrime(num) {
    //Negative, 0, 1 is not a prime number
    if (num <= 1) return false;

    var b = true; //Assume num is a prime
    for (let i = 2; i < num; i++) {
      if (num % i == 0) {
        //If any i could be devided, it is not a prime number
        b = false;
        break;
      }
    }

    return b;
  }
};