const dotenv = require('dotenv')
dotenv.config();

const accountSid = process.env.TWILIO_ACCOUNT_SID
const authToken = process.env.TWILIO_AUTH
const client = require('twilio')(accountSid, authToken);

client.conversations.v1.conversations('')
                       .participants
                       .create({identity: 'testPineapple'})
                       .then(participant => console.log(participant.sid));
