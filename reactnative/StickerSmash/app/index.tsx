import React, { useState, useRef, useEffect } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity, Linking, Alert } from 'react-native';
import { useRouter } from 'expo-router';
import PhoneInput from 'react-native-phone-input';

export default function Index() {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [verificationCode, setVerificationCode] = useState('');
  const [isVerificationScreen, setIsVerificationScreen] = useState(false);
  const [attempts, setAttempts] = useState(0);
  const router = useRouter();
  const codeInputs = useRef([]);

  useEffect(() => {
    if (isVerificationScreen) {
      codeInputs.current[0]?.focus();
    }
  }, [isVerificationScreen]);

  const handleNext = () => {
    if (phoneNumber.trim()) {
      setIsVerificationScreen(true);
    } else {
      Alert.alert('Error', 'Please enter a valid phone number.');
    }
  };

  const handleVerify = () => {
    if (verificationCode === '123456') { // Replace with actual verification logic
      router.replace('/messages');
    } else {
      setAttempts(attempts + 1);
      if (attempts >= 4) {
        Alert.alert('Error', 'Too many failed attempts. Exiting app.');
        // Exit app logic here
      } else {
        Alert.alert('Error', 'Invalid verification code. Please try again.');
      }
    }
  };

  const handleKeyPress = (index, key) => {
    if (key >= '0' && key <= '9') {
      const newCode = verificationCode.split('');
      newCode[index] = key;
      setVerificationCode(newCode.join(''));
      if (index < 5) {
        codeInputs.current[index + 1].focus();
      } else {
        handleVerify();
      }
    }
  };

  return (
    <View style={styles.container}>
      {!isVerificationScreen ? (
        <>
          <Text style={styles.title}>Welcome to login TrueUp</Text>
          <Text style={styles.instructions}>Get a one-time verification code from your phone.</Text>
          <PhoneInput
            style={styles.phoneInput}
            initialCountry="us"
            value={phoneNumber}
            onChangePhoneNumber={setPhoneNumber}
          />
          <TouchableOpacity style={styles.button} onPress={handleNext}>
            <Text style={styles.buttonText}>Next</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={() => Linking.openURL('https://www.gettrueup.com/legal/terms-of-service')}>
            <Text style={styles.link}>Terms and Service</Text>
          </TouchableOpacity>
        </>
      ) : (
        <>
          <Text style={styles.title}>Enter Verification Code</Text>
          <View style={styles.codeContainer}>
            {[...Array(6)].map((_, index) => (
              <TextInput
                key={index}
                ref={(ref) => (codeInputs.current[index] = ref)}
                style={styles.codeInput}
                keyboardType="number-pad"
                maxLength={1}
                value={verificationCode[index] || ''}
                onChangeText={() => {}}
                onKeyPress={({ nativeEvent: { key } }) => handleKeyPress(index, key)}
              />
            ))}
          </View>
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  instructions: {
    fontSize: 16,
    marginBottom: 20,
    textAlign: 'center',
  },
  phoneInput: {
    width: '100%',
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#008000',
    padding: 15,
    borderRadius: 5,
    marginBottom: 20,
    width: '100%',
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
  link: {
    color: '#008000',
    textDecorationLine: 'underline',
  },
  codeContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '80%',
  },
  codeInput: {
    width: 40,
    height: 40,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    textAlign: 'center',
    fontSize: 18,
  },
});