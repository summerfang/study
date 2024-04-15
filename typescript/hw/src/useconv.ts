import { getContacts } from "./data";
import { json } from "@remix-run/node"

export const getC = async () => {
    const contacts = await getContacts();
    return contacts;
  };

var a: object;

const cons = getC()
console.log(cons);

cons.then((o) => {
    console.log(o.length);
    a = o;
},
()=>{})

console.log(a);