import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, TextInput, ScrollView, Linking } from 'react-native';
import Ionicons from '@expo/vector-icons/Ionicons';

type Message = {
  id: string;
  text: string;
  type: 'incoming' | 'outgoing';
  time: string;
};

export default function NewMessageDetailScreen() {
  // Example data with 12 total messages
  const [messages, setMessages] = useState<Message[]>([
    { id: '1', text: 'Hello there! This is an example of a multi-line incoming message.', type: 'incoming', time: '10:31 AM' },
    { id: '2', text: 'Hi! Good to see you. This is an outgoing message example.', type: 'outgoing', time: '10:32 AM' },
    { id: '3', text: 'Sure, let’s meet later?', type: 'outgoing', time: '10:33 AM' },
    { id: '4', text: 'Yes, absolutely! Looking forward to it.', type: 'incoming', time: '10:34 AM' },
    { id: '5', text: 'Just a short one-liner.', type: 'incoming', time: '10:35 AM' },
    { id: '6', text: 'This is a much longer message that demonstrates how text can wrap across multiple lines. It is still considered incoming, so it should use the grey bubble.', type: 'incoming', time: '10:36 AM' },
    { id: '7', text: 'Let me know when you’re free?', type: 'outgoing', time: '10:37 AM' },
    { id: '8', text: 'I’m free after lunch around 1 PM.', type: 'incoming', time: '10:38 AM' },
    { id: '9', text: 'Perfect. I’ll see you then!', type: 'outgoing', time: '10:39 AM' },
    { id: '10', text: 'Can we finalize the report today?', type: 'incoming', time: '10:40 AM' },
    { id: '11', text: 'Yes, I’ll send it over soon.', type: 'outgoing', time: '10:41 AM' },
    { id: '12', text: 'Great, thanks a lot!', type: 'incoming', time: '10:42 AM' },
  ]);
  const [inputText, setInputText] = useState('');

  const initials = 'JD'; // Example initials
  const name = 'John Doe';
  const lastMessageTime = '10:42 AM';

  const handleCall = () => {
    Linking.openURL('tel:123456789'); // Replace with the actual number
  };

  const handleMenu = () => {
    alert('Menu button pressed.');
  };

  const handleSend = () => {
    if (!inputText.trim()) return;

    setMessages((prev) => [
      ...prev,
      { id: Date.now().toString(), text: inputText, type: 'outgoing', time: 'Just now' },
    ]);
    setInputText('');
  };

  return (
    <View style={styles.container}>
      {/* Header Section */}
      <View style={styles.header}>
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>{initials}</Text>
        </View>
        <View style={styles.headerInfo}>
          <Text style={styles.name}>{name}</Text>
          <Text style={styles.lastTime}>{`Last message: ${lastMessageTime}`}</Text>
        </View>
        <TouchableOpacity onPress={handleCall} style={styles.iconButton}>
          <Ionicons name="call-outline" size={24} color="#fff" />
        </TouchableOpacity>
        <TouchableOpacity onPress={handleMenu} style={styles.iconButton}>
          <Ionicons name="ellipsis-vertical" size={24} color="#fff" />
        </TouchableOpacity>
      </View>

      {/* Messages Section */}
      <ScrollView style={styles.messagesContainer}>
        {messages.map((msg) => {
          const isIncoming = msg.type === 'incoming';
          return (
            <View
              key={msg.id}
              style={[
                styles.messageBubble,
                isIncoming ? styles.incomingBubble : styles.outgoingBubble,
              ]}
            >
              <Text style={isIncoming ? styles.incomingText : styles.outgoingText}>
                {msg.text}
              </Text>
              <Text style={styles.messageTime}>{msg.time}</Text>
            </View>
          );
        })}
      </ScrollView>

      {/* Input Section */}
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Type your message here..."
          placeholderTextColor="#888"
          value={inputText}
          onChangeText={setInputText}
          multiline
        />
        <TouchableOpacity onPress={handleSend} style={styles.sendButton}>
          <Ionicons name="send" size={20} color="#fff" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const bubbleRadius = 16;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#25292e',
    paddingHorizontal: 10,
    paddingTop: 40,
    paddingBottom: 10,
  },
  avatar: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 10,
  },
  avatarText: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  headerInfo: {
    flex: 1,
    justifyContent: 'center',
  },
  name: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
  },
  lastTime: {
    fontSize: 12,
    color: '#fff',
  },
  iconButton: {
    padding: 8,
    marginLeft: 10,
  },
  messagesContainer: {
    flex: 1,
    paddingHorizontal: 10,
    paddingTop: 10,
  },
  messageBubble: {
    maxWidth: '80%',
    padding: 10,
    marginBottom: 10,
    borderRadius: bubbleRadius,
  },
  incomingBubble: {
    backgroundColor: '#ccc',
    alignSelf: 'flex-start',
    borderTopLeftRadius: bubbleRadius * 2,
    borderBottomLeftRadius: bubbleRadius * 2,
  },
  outgoingBubble: {
    backgroundColor: '#008000',
    alignSelf: 'flex-end',
    borderTopRightRadius: bubbleRadius * 2,
    borderBottomRightRadius: bubbleRadius * 2,
  },
  incomingText: {
    color: '#000',
  },
  outgoingText: {
    color: '#fff',
  },
  messageTime: {
    alignSelf: 'flex-end',
    fontSize: 10,
    color: '#888',
    marginTop: 5,
  },
  inputContainer: {
    flexDirection: 'row',
    padding: 10,
    backgroundColor: '#25292e',
    alignItems: 'center',
  },
  input: {
    flex: 1,
    minHeight: 40,
    maxHeight: 80,
    backgroundColor: '#fff',
    borderRadius: 20,
    paddingHorizontal: 15,
    color: '#000',
  },
  sendButton: {
    backgroundColor: '#00ff00',
    borderRadius: 20,
    width: 40,
    height: 40,
    marginLeft: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
});