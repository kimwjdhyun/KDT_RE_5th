void setup() {
  pinMode(3, OUTPUT);

}

void loop() {
  analogWrite(3, 255);
  delay(200);
  analogWrite(3, 191);
  delay(200);
  analogWrite(3, 127);
  delay(200);
  analogWrite(3, 64);
  delay(200);
  analogWrite(3, 0);
  delay(200);
}
