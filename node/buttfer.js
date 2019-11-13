var str = Buffer.from("Hello World!", 'ascii');
console.log(str.toString('hex'));
console.log(str.toString('base64'))

str = Buffer.from([0x1, 0x2, 0x3, 0x4]);
const json = JSON.stringify(str);

console.log(json);

const copy = JSON.parse(json, (key, value)=>{
    return value && value.type === 'Buffer' ? 
        Buffer.from(value.data) : 
        value;
});

console.log(copy);