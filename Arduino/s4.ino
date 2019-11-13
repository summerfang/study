int brightness = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(9,OUTPUT)
}

void loop() {
  // put your main code here, to run repeatedly:
  if(brightness + 5 > 255)
    brightness = 255 - (5 - abs(255 - brightness))
  digitalWrite(9, brightness);
}
