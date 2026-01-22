void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
}

void loop() {
  int light = analogRead(A0);
  Serial.println(light);
  delay(500);

  if (light > 1000)
    digitalWrite(8, HIGH);
  else
    digitalWrite(8, LOW);
}
