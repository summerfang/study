const dotenv = require('dotenv')
dotenv.config();

// Download the helper library from https://www.twilio.com/docs/node/install
// Find your Account SID and Auth Token at twilio.com/console
// and set the environment variables. See http://twil.io/secure
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

client.conversations.v1.conversations
    .create({ friendlyName: 'My second Conversation' })
    .then(conversation => {
        console.log(conversation.sid);

        client.conversations.v1.conversations(conversation.sid)
            .fetch()
            .then(conversation => console.log(conversation.chatServiceSid));

        // client.conversations.v1.conversations(conversation.sid)
        //     .participants
        //     .create({
        //         'messagingBinding.address': '+14088323545',
        //         'messagingBinding.proxyAddress': '+18559563669'
        //     })
        //     .then(participant => console.log(participant.sid));

        client.conversations.v1.conversations(conversation.sid)
            .participants
            .create({ identity: 'testPineapple' })
            .then(participant => {
                console.log(participant.sid);
                
            });
    });
