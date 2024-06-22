// import { getToken4email } from "./getToken4email";

// try {
//     let token = await getToken4email('summerfang@gmail.com');
// } catch {
//     throw new Error("Unable to get token")
// }
const Chat = require("twilio-chat");

async function getToken4email(email) {
    const response = await fetch(`http://localhost:5000/token/${email}`);
    const data = await response.json();
    return data;
}

const email = 'summerfang@gmail.com';
const response = getToken4email(email);
response
    .then(async (data) => {
        // Now 'data' contains the parsed JSON object
        console.log(data.token);

        const client = new Chat.Client.create(data.token);

        // client.on("tokenAboutToExpire", async () => {
        //     const data = await getToken4email(email);
        //     client.updateToken(data.token);
        // });

        // client.on("tokenExpired", async () => {
        //     const data = await getToken4email(email);
        //     client.updateToken(data.token);
        // });

        const channel = await client.createChannel({
            uniqueName: 'general',
            friendlyName: 'general'
        });

        channel.then((result)=>result.json())
        .then((d)=>console.log(d))
    })

// const data = response.json();
// console.log(data);

// export { };
