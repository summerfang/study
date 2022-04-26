function printRevese(str) {
    if (str.length == 0)
        return
    else {
        printRevese(str.substr(1))
        process.stdout.write(str.charAt(0))
    }
}

var str = "Hello World!";
printRevese(str);
console.log("\n");
