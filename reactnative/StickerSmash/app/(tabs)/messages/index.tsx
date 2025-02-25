import React from 'react';
import { Text, View, StyleSheet, TextInput, FlatList, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const messages = [
  {
    id: '1',
    avatar: 'https://example.com/avatar1.png',
    name: 'John Doe',
    message: 'Hey, how are you?',
    time: '10:30 AM',
    unread: 2,
  },
  {
    id: '2',
    avatar: 'https://example.com/avatar2.png',
    name: 'Jane Smith',
    message: 'Are we still on for tomorrow?',
    time: '9:15 AM',
    unread: 1,
  },
  {
    id: '3',
    avatar: 'https://example.com/avatar3.png',
    name: 'Alice Johnson',
    message: 'Can you send me the report?',
    time: '8:45 AM',
    unread: 0,
  },
  {
    id: '4',
    avatar: 'https://example.com/avatar4.png',
    name: 'Bob Brown',
    message: 'Meeting at 3 PM.',
    time: '8:00 AM',
    unread: 3,
  },
  {
    id: '5',
    avatar: 'https://example.com/avatar5.png',
    name: 'Charlie Davis',
    message: 'Lunch tomorrow?',
    time: '7:30 AM',
    unread: 1,
  },
  {
    id: '6',
    avatar: 'https://example.com/avatar6.png',
    name: 'David Evans',
    message: 'Project update?',
    time: '7:00 AM',
    unread: 0,
  },
  {
    id: '7',
    avatar: 'https://example.com/avatar7.png',
    name: 'Eva Green',
    message: 'Call me when you can.',
    time: '6:30 AM',
    unread: 2,
  },
  {
    id: '8',
    avatar: 'https://example.com/avatar8.png',
    name: 'Frank Harris',
    message: 'Good morning!',
    time: '6:00 AM',
    unread: 0,
  },
  {
    id: '9',
    avatar: 'https://example.com/avatar9.png',
    name: 'Grace Lee',
    message: 'See you soon.',
    time: '5:30 AM',
    unread: 1,
  },
  {
    id: '10',
    avatar: 'https://example.com/avatar10.png',
    name: 'Henry Miller',
    message: 'Thanks!',
    time: '5:00 AM',
    unread: 0,
  },
  {
    id: '11',
    avatar: 'https://example.com/avatar11.png',
    name: 'Ivy Nelson',
    message: 'Got it.',
    time: '4:30 AM',
    unread: 0,
  },
  // Add more messages as needed
];

export default function MessagesScreen() {
  return (
    <View style={styles.container}>
      <TextInput
        style={styles.searchBar}
        placeholder="Search..."
        placeholderTextColor="#888"
      />
      <FlatList
        data={messages}
        renderItem={({ item }) => <MessageRow message={item} />}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.content}
      />
    </View>
  );
}

function MessageRow({ message }) {
  const navigation = useNavigation();
  const initials = message.name.split(' ').map(name => name[0]).join('').toUpperCase();

  return (
    <TouchableOpacity onPress={() => navigation.navigate('MessageDetail', { name: message.name, messages: [message.message] })}>
      <View style={styles.row}>
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>{initials}</Text>
        </View>
        <View style={styles.messageContent}>
          <View style={styles.messageHeader}>
            <Text style={styles.name}>{message.name}</Text>
            <Text style={styles.time}>{message.time}</Text>
          </View>
          <View style={styles.messageBody}>
            <Text style={styles.messageText}>{message.message}</Text>
            {message.unread > 0 && (
              <View style={styles.unreadBadge}>
                <Text style={styles.unreadText}>{message.unread}</Text>
              </View>
            )}
          </View>
        </View>
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    paddingTop: 20,
  },
  searchBar: {
    width: '90%',
    height: 40,
    backgroundColor: '#fff',
    borderRadius: 20,
    paddingHorizontal: 15,
    alignSelf: 'center',
    marginBottom: 20,
  },
  content: {
    paddingHorizontal: 10,
  },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#444',
  },
  avatar: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 10,
  },
  avatarText: {
    color: '#000',
    fontSize: 18,
    fontWeight: 'bold',
  },
  messageContent: {
    flex: 1,
  },
  messageHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  name: {
    fontWeight: 'bold',
    fontSize: 16,
    color: '#fff',
  },
  time: {
    fontSize: 12,
    color: '#888',
  },
  messageBody: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  messageText: {
    fontSize: 14,
    color: '#aaa',
  },
  unreadBadge: {
    backgroundColor: '#00ff00',
    borderRadius: 10,
    paddingHorizontal: 6,
    paddingVertical: 2,
    marginLeft: 10,
  },
  unreadText: {
    color: '#fff',
    fontSize: 12,
  },
});
