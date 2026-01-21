void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop() {
  int resistor = analogRead(A0);
  Serial.println(resistor);

  resistor = resistor / 4;
  
  analogWrite(9, resistor);
  delay(100);
}