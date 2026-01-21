int btn = 12;


void setup() {
Serial.begin(9600);
pinMode(btn, INPUT_PULLUP); // 기본 상태가 1, 스위치가 눌렸을 때 0

}

void loop() {
  int btnstate = digitalRead(btn);
  Serial.println(btnstate);
  delay(500);

}
