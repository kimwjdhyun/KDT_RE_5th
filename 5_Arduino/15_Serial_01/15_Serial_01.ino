int data;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, Low);
}

void loop() {
  while (Serial.available()) { // 시리얼 통신이 가능한지 확인 및 시리얼 통신이 되는 동안 아래 스코프 코드 반복
    data = Serial.read(); // 아두이노가 PC에서 받은 1바이트를 가져와 data 변수에 저장
  }
  if (data = "1"){
    digitalWrite(13, HIGH);
  } else if (13, LOW);
}
