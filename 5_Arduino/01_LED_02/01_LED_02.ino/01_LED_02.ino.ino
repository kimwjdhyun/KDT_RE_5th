/* 
ctrl + n : 아두이노 새 스케치 열기

새로운 스케치를 열면 새로운 창이 열림

아두이노 IDE에서는 탭 방식이 아닌 여러 창을 사용하는 방식이기 때문

스케치 = 하나의 폴더
폴더 = 하나의 독립 프로젝트
그렇기 때문에 프로젝트마다 별도의 창이 생기고 사용하는 것

--------

폴더 = 하나의 독립 프로젝트
그래서 .ino 파일은 새로운 폴더 안에 생기

아두이노는 폴더 이름과 동일한 .ino 파일을 "메인 파일"로 간주함
같은 폴더 안의 .ino 파일은 하나의 코드처럼 합쳐서 컴파일

즉, 하나의 스케치 폴더 안에는 .ino 파일이 여러개 있으면
하나의 큰 코드로 인식

하나의 스케치 폴더 안에는 set up(), loop()가 단 하나씩만 존재해야함
*/


int LED_pin1 = 10;
int LED_pin2 = 11;
int LED_pin3 = 12;

void setup() {
  pinMode(LED_pin1, OUTPUT);
  pinMode(LED_pin2, OUTPUT);
  pinMode(LED_pin3, OUTPUT);
}

// version 1 
void loop() {
  digitalWrite(LED_pin1, HIGH);
  delay(500);
  digitalWrite(LED_pin1, LOW);
  delay(500);
  digitalWrite(LED_pin2, HIGH);
  delay(500);
  digitalWrite(LED_pin2, LOW);
  delay(500);
  digitalWrite(LED_pin3, HIGH);
  delay(500);
  digitalWrite(LED_pin3, LOW);
  delay(500);
}
                                                                                         