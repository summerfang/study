import { Conversation } from "@twilio/conversations";

const dotenv = require('dotenv')
dotenv.config();

const accountSid = process.env.TWILIO_ACCOUNT_SID
const authToken = process.env.TWILIO_AUTH

const client = require('twilio')(accountSid, authToken);

let cid = ''
client.conversations.v1.conversations
                       .create({friendlyName: 'My First Conversation'})
                       .then((conversation : Conversation) => {
                          console.log(conversation.sid);
                          cid = conversation.sid;
                        });


// client.conversations.v1.conversations(cid)
//                         .fetch()
//                         .then((conversation) => console.log(conversation.chatServiceSid));
