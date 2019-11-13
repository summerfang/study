int PORT = 10;

void setup() {
  // put your setup code here, to run once:
  pinMode(PORT, 10);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i = 0;

  for(i = 0; i < 3; i++) {
      digitalWrite(PORT, HIGH);
      delay(150);
      digitalWrite(PORT, LOW);
      delay(100);
    }

  for(i = 0; i < 3; i++) {
      digitalWrite(PORT, HIGH);
      delay(400);
      digitalWrite(PORT, LOW);
      delay(100);
    }

  for(i = 0; i < 3; i++) {
      digitalWrite(PORT, HIGH);
      delay(150);
      digitalWrite(PORT, LOW);
      delay(100);
    }

}
