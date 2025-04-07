import React from 'react';
import { Text, View, StyleSheet, TextInput, FlatList, TouchableOpacity } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const messages = [
  {
    id: '1',
    name: 'John Doe',
    message: 'Hey, how are you?',
    time: '10:30 AM',
    unread: 2,
  },
  {
    id: '2',
    name: 'Jane Smith',
    message: 'Hey, did you finalize the design?',
    time: '11:00 AM',
    unread: 0,
  },
  {
    id: '3',
    name: 'Mark Johnson',
    message: 'Let’s schedule a call later.',
    time: '12:15 PM',
    unread: 1,
  },
  {
    id: '4',
    name: 'Sara Lee',
    message: 'Awesome! I’ll check it out now.',
    time: '1:30 PM',
    unread: 0,
  },
  {
    id: '5',
    name: 'David Park',
    message: 'Could you explain the new feature?',
    time: '2:05 PM',
    unread: 1,
  },
  {
    id: '6',
    name: 'Emily Carter',
    message: 'Thanks for the update!',
    time: '2:20 PM',
    unread: 0,
  },
  {
    id: '7',
    name: 'Peter Brown',
    message: 'Lunch at 1:00?',
    time: '10:45 AM',
    unread: 0,
  },
  {
    id: '8',
    name: 'Jessica Martin',
    message: 'Please review the PR.',
    time: '4:10 PM',
    unread: 3,
  },
  {
    id: '9',
    name: 'Kevin Adams',
    message: 'We need to discuss the budget.',
    time: '5:00 PM',
    unread: 1,
  },
  {
    id: '10',
    name: 'Anna Moore',
    message: 'Let me know what you think!',
    time: '5:30 PM',
    unread: 2,
  },
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
    <TouchableOpacity
      onPress={() =>
        navigation.navigate('newmessagedetail', {
          name: message.name,
          messages: [message.message],
        })
      }
    >
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
