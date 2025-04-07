import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

import { RouteProp } from '@react-navigation/native';

type RouteParams = {
    params: {
        name: string;
        messages: string[];
    };
};

export default function MessageDetailScreen({ route }: { route: RouteProp<RouteParams, 'params'> }) {
    const { name, messages } = route.params;

    return (
        <View style={styles.container}>
            <Text style={styles.title}>{name}</Text>
            {messages.map((msg, index) => (
                <Text key={index} style={styles.message}>{msg}</Text>
            ))}
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#25292e',
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#fff',
        marginBottom: 20,
    },
    message: {
        fontSize: 16,
        color: '#fff',
        marginBottom: 10,
    },
});