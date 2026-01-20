int LEDS[] = {10, 11, 12};
int count = 3;



void blinkALL(bool state) {
  for (int i = 0; i < count; i++) {
    digitalWrite(LEDS[i], state ? HIGH : LOW);

  // state ? HIGH : LOW
  //  => 조건 ? true일 때 반환할 값 : false일 때 반환할 값
  // 삼항연산자 : if 문을 아주 짧게 줄여놓은 것

  // if state == true:
  //    return HIGH
  // else:
  //    return LOW

  // delay(500);
  }
  delay(500);
}

void setup() {
  for (int i = 0; i < count; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  blinkALL(true);
  blinkALL(false);
}