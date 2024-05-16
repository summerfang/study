import { createToken4Identity } from "./createToken4identity";

let strToken = createToken4Identity('summerfang@gmail.com');

console.log(strToken)

/* Initialization */
import {Client} from "@twilio/conversations";

const client = new Client(strToken);
client.on("stateChanged", (state) => {
    console.log(state);
    
    if (state === "failed") {
        // The client failed to initialize
        return;
    }

    if (state === "initialized") {
        // Use the client
    }
});
