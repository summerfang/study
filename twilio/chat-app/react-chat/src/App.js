import logo from './logo.svg';
import './App.css';
// import { getToken4email } from './getToken4email';
import { useEffect, useState } from 'react';
const Chat = require("twilio-chat");

function App() {
  // const token = getToken4email('summerfang@gmail.com');
  // const email = 'summerfang@gmail.com'
  // const response = fetch(`http://localhost:5000/token/${email}`);
  // response.then((result)=>{

  // })
  var chatClient;
  // var username;
  var generalChannel;

  const [message, setMessage] = useState({})
  const [token, setToken] = useState('');
  const [username, setUserName] = useState('')

  const getToken = async (email) => {
    // const email = 'summerfang@gmail.com';
    const res = await fetch(`http://localhost:5000/token/${email}`);
    const data = await res.json();
    return data;
  }

  useEffect(() => {
    getToken('summerfang@gmail.com')
      .then((data) => {
        console.log(data.token)
        setToken(data.token);
        setUserName(data.identity)

        Chat.Client.create(data.token)
          .then(client => {
            chatClient = client;
            
            chatClient.getSubscribedChannels().then(()=>{
              chatClient.getChannelByUniqueName('general')
                .then(
                  (channel) => {
                    generalChannel = channel;
                    generalChannel.join()
                      .then((channel) => {

                      });
                    
                      generalChannel.on('messageAdded', function(msg) {

                      })
                      .catch()
                  }
                )
            });

            // // when the access token is about to expire, refresh it
            // chatClient.on('tokenAboutToExpire', function () {
            //   refreshToken(username);
            // });

            // // if the access token already expired, refresh it
            // chatClient.on('tokenExpired', function () {
            //   refreshToken(username);
            // });
          })
      })

  }, []);

  // function refreshToken(identity) {
  //   console.log('Token about to expire');
  //   // Make a secure request to your backend to retrieve a refreshed access token.
  //   // Use an authentication mechanism to prevent token exposure to 3rd parties.
  //   $.getJSON('/token/' + identity, function(data) {
  //     console.log('updated token for chat client');          
  //     chatClient.updateToken(data.token);
  //   });
  // }

  function createOrJoinGeneralChannel() {
    // Get the general chat channel, which is where all the messages are
    // sent in this simple application
    // print('Attempting to join "general" chat channel...');
    chatClient.getChannelByUniqueName('general')
      .then(function (channel) {
        generalChannel = channel;
        console.log('Found general channel:');
        console.log(generalChannel);
        setupChannel();
      }).catch(function () {
        // If it doesn't exist, let's create it
        console.log('Creating general channel');
        chatClient.createChannel({
          uniqueName: 'general',
          friendlyName: 'General Chat Channel'
        }).then(function (channel) {
          console.log('Created general channel:');
          console.log(channel);
          generalChannel = channel;
          setupChannel();
        }).catch(function (channel) {
          console.log('Channel could not be created:');
          console.log(channel);
        });
      });
  }

  // Set up channel after it has been found
  function setupChannel() {
    // Join the general channel
    generalChannel.join().then(function (channel) {
      // print('Joined channel as '
      //   + '<span class="me">' + username + '</span>.', true);
    });

    // Listen for new messages sent to the channel
    generalChannel.on('messageAdded', function (msg) {
      // printMessage(message.author, message.body);
      // setMessage(msg);
    });
  }

  // useEffect( () => {
  //   token = getToken('summerfang@gmail.com')
  //           .then((token)=>{
  //             setToken(token)

  //           })

  // token = await getToken('summerfang@gmail.com');
  // const client = await Chat.Client.create(token);

  // client.on("tokenAboutToExpire", async () => {
  //   const token = await getToken('summerfang@gmail.com');
  //   client.updateToken(token);
  // });

  // client.on("tokenExpired", async () => {
  //   const token = await this.getToken('summerfang@gmail.com');
  //   client.updateToken(token);
  // });

  // client.on("channelJoined", async (channel) => {
  //   // getting list of all messages since this is an existing channel
  //   const messages = await channel.getMessages();
  //   // this.setState({ messages: messages.items || [] });
  //   // this.scrollToBottom();
  // });

  // try {
  //   const channel = await client.getChannelByUniqueName({
  //     uniqueName: 'general',
  //     friendlyName: 'general',
  //   });
  // } catch (err) {
  //   try {
  //     const channel = await client.createChannel({
  //       uniqueName: 'general',
  //       friendlyName: 'general',
  //     });

  //     channel.sendMessage(String('Hello world').trim())

  //   } catch {
  //     throw new Error("Unable to create channel, please reload this page");

  //   }
  // }


  // }
  //   , [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        <p>
          Token: {token}
        </p>
        <p>
          New message: from {username}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
