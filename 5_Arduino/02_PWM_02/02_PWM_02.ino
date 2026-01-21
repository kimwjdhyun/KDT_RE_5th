int LED_PIN = 3;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  for (int i = 0; i <= 255; i++) {
    analogWrite(LED_PIN, i);
    delay(10);
  }
  
  for (int i = 255; i >= 0; i--) {
    analogWrite(LED_PIN, i);
    delay(10);
  }
  Serial.println(i); // println : 출력 + 줄바꿈
}

/*
Serial: 시리얼 통신을 담당하는 객체
  시리얼 통신 : 글자, 숫자, 데이터를 주고 받는 통신

Serial.begin(9600);
- 아두이노가 pc와 통신하기 위해 시리얼 통신을 시작하겠다 명시하는 코드
- 매개변수로 넣은 값 속도로 시리얼 통신을 시작함
- 통신 속도는 대체로 9600을 사용(오래 전부터 사용해온 안정적이고 에러 없는 표준 속도, 
  통신속도가 너무 빠르면 데이터 손실, 느리면 데이터 전송 불편.
  거의 모든 장치가 지원하는 속도)
- setup() 함수 내에 한 번만 작성하면 됨

Serial.print();
- 아두이노에서 PC(시리얼 모니터)로 문자나 숫자, 변수값을 보내주는 함수
- 통신 상태 or 디버깅용으로 사용
*/