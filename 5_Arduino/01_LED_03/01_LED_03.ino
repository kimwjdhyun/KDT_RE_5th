int LED_pin1 = 10;
int LED_pin2 = 11;
int LED_pin3 = 12;

void setup() {
  pinMode(LED_pin1, OUTPUT);
  pinMode(LED_pin2, OUTPUT);
  pinMode(LED_pin3, OUTPUT);
}

// version 2 : 모든 LED가 켜진 뒤 0.5초 동안 유지하고, 모든 LED를 끈 뒤 0.5초 유지
void loop() {
  digitalWrite(LED_pin1, HIGH);
  digitalWrite(LED_pin1, HIGH);
  digitalWrite(LED_pin2, HIGH);
  delay(500);
  digitalWrite(LED_pin2, LOW);
  digitalWrite(LED_pin3, LOW);
  digitalWrite(LED_pin3, LOW);
  delay(500);
}