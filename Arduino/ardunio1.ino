int port = 13;
void setup() {
  // put your setup code here, to run once:
  pinMode(port, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(port, HIGH);
  delay(1000);
  digitalWrite(port, LOW);
  delay(500);
}
