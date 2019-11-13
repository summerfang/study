void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int iStatus = digitalRead(2);
  Serial.println(iStatus);
  delay(1);
}
