const dotenv = require('dotenv')
dotenv.config();

const accountSid = process.env.TWILIO_ACCOUNT_SID
const authToken = process.env.TWILIO_AUTH
const client = require('twilio')(accountSid, authToken);

client.conversations.v1.conversations
    .create({ friendlyName: 'Chat Room #1' })
    .then(conversation => {
        console.log(`conversation.sid=` + conversation.sid);
        let cid = conversation.sid;

        client.conversations.v1.conversations(cid)
            .fetch()
            .then(conversation => console.log('conversation.chatServiceSid=' + conversation.chatServiceSid));

        client.conversations.v1.conversations(cid)
            .participants
            .create({
                'messagingBinding.address': '+14088323545',
                'messagingBinding.proxyAddress': '+18559563669'
            })
            .then(
                participant => console.log('participant.sid='+participant.sid), 
                (e)=>(console.log('error=' + e))
        );

    });


