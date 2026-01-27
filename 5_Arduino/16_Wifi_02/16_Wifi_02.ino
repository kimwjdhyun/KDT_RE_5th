#include <SoftwareSerial.h>

SoftwareSerial myESP(2, 3); // D2=RX(ESP TX), D3=TX(ESP RX)

// ESP 모델 속도가 9600으로 바뀌었는지 확인
void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("=== TEST 9600 ===");

}

void loop() {
  if (myESP.available()) {
    Serial.write(myESP.read());
  }
  if (Serial.available()) {
    myESP.write(Serial.read());
  }
}


//공유기 연결하는 명령어
//AT+CWJAP="spreatics_gusan_cctv","spreatics*"