#define PUMP_PIN 9

void setup() {
  Serial.begin(9600);
  pinMode(PUMP_PIN, OUTPUT);
  digitalWrite(PUMP_PIN, LOW);
  Serial.println("펌프 테스트 시작");
}

void loop() {
  Serial.println("펌프 ON");
  digitalWrite(PUMP_PIN, HIGH);
  delay(3000);

  Serial.println("펌프 OFF");
  digitalWrite(PUMP_PIN, LOW);
  delay(3000);
}
