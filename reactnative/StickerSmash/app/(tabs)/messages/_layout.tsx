import { Tabs } from 'expo-router';

import Ionicons from '@expo/vector-icons/Ionicons';

export default function MessagesLayout() {
    return (
        <Tabs
            screenOptions={{
                tabBarActiveTintColor: '#00ff00', // Changed to green
                headerStyle: {
                    backgroundColor: '#25292e',
                },
                headerShadowVisible: false,
                headerTintColor: '#fff',
                tabBarStyle: {
                    backgroundColor: '#25292e',
                },
            }}
        >

            <Tabs.Screen
                name="message"
                options={{
                    title: 'Messages',
                    tabBarIcon: ({ color, focused }) => (
                        <Ionicons name={focused ? 'chatbubbles' : 'chatbubbles-outline'} color={color} size={24} />
                    ),
                }}
            />
        </Tabs>
    );
}
