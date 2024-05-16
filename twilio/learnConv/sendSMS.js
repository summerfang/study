const dotenv = require('dotenv')
dotenv.config();

// Download the helper library from https://www.twilio.com/docs/node/install
// Find your Account SID and Auth Token at twilio.com/console
// and set the environment variables. See http://twil.io/secure
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

const messagingServiceSid = process.env.TWILIO_CHAT_SERVICE_SID;

client.messages
    .create({
        body: 'Hello again! this is Summer Fang',
        from: '+18559563669',
        to: '+18777804236'
    })
    .then(message => console.log(message.sid));
    // .done();