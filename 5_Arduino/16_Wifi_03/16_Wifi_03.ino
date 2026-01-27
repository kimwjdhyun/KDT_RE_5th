#include <SoftwareSerial.h>
#include <DHT.h>

SoftwareSerial myESP(2, 3);
#define DHT_PIN 4
#define DHTTYPE DHT11
DHT mydht(DHT_PIN, DHTTYPE);


const char *ssid = "spreatics_gusan_cctv";
const char *password = "spreatics*";
const char *server = "192.168.201.103";
const int port = 5000;

// ESP 모듈 AT 명령을 보내서 응답 중 특정 단어가 나올 때 까지 기다리는 함수
// 예) 명령 처리를 완료했으면 OK를 보내라고 지정했을 때 OK가 올 때까지 해당 함수가 실행

// bool : sendCommand 함수의 리턴될 값 자료형
// cmd : 보낼 명령
// expect : 응답에서 원하는 문자열
// timeout : 기다릴 시간

bool sendCommand(String cmd, String expect, int timeout) {
  myESP.print(cmd);
  myESP.print("\r\n");

  unsigned long t = millis(); // 함수 시작 시간을 저장해 종료 시간을 계산하기 위한 변수
  String buf; // ESP가 보낸 문자열을 합칠 변수

  while (millis() - t < timeout) { // 매개변수로 전달받은 timeout 시간 동안만 동작하게 하는 반복문
    while (myESP.available()) {
      char c = myESP.read(); // ESP-01이 보낸 데이터 한 글자씩 읽어오기
      buf += c; // 읽은 글자 buf 변수에 이어붙이기
      Serial.write(c);

      if(buf.indexOf(expect) != -1) { // 전달받은 문자열 중에서 내가 원하던 단어가 있으면 true 리턴
        return true;
      }
    }
  }
  return false; // 제한 시간 내 원하는 단어가 출력되지 않았으면 false 리턴
}

void sendDataToServer(int temp, int hum) {
  // 쿼리스트링 HTTP GET 요청 경로 작성
  String url = "/data?temperature=" + String(temp) + "&humidity=" + String(hum);  // Stirng → String, 세미콜론 추가

  // AT + CIPSTART : 서버와 TCP 연결
  if(!sendCommand("AT+CIPSTART=\"TCP\",\"" + String(server) + "\"," + String(port), "CONNECT", 5000)) {  // 세미콜론 제거, 중괄호 위치 수정, String(port) 추가
    return;
  }

  String req = "GET " + url + " HTTP/1.1\r\n"  // Stirng → String, GET 뒤 공백 추가, HTTP 앞 공백 추가
               "Host: " + String(server) + ":" + String(port) + "\r\n"  // Host 뒤 공백 제거
               "Connection: close\r\n\r\n";  // close 뒤 공백 제거

  if(sendCommand("AT+CIPSEND=" + String(req.length()), ">", 3000)) { // ">" 나올때 까지 3초 기다림
    myESP.print(req); // HTTP 전송
    sendCommand("", "SEND OK", 4000); // ESP가 OK라고 할때 까지 4초 기다림 -> 데이터 전송 완료를 기다리는 것
  }

  sendCommand("AT+CIPCLOSE", "OK", 2000); // AT+CIPCLOSE : TCP 연결 종료
  Serial.println("\n[전송 완료]");  // 공백 제거
} 

void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("ESP 실행 시작...");
  mydht.begin();

  sendCommand("AT", "OK", 2000); // ESP 정상 연결 확인
  sendCommand("AT+CWMODE=1", "OK", 2000); // ESP 일반 wifi 기기 모드로 설정
  sendCommand(String("AT+CWJAP=\"") + ssid + "\",\"" + password + "\"", "GOT IP", 15000); // Stirng → String, CWFAP → CWJAP
  sendCommand("AT+CIPMUX=0", "OK", 2000); // 한 번의 연결에 데이터는 한 번만 주고 받겠다.
}

void loop() { // 5초에 한번씩 sendDataToServer 함수를 실행 시켜 서버로 데이터 전송
  delay(2000);
  float h = mydht.readHumidity();
  float c = mydht.readTemperature();
  sendDataToServer(c, h);
  delay(5000);

    if (isnan(h) || isnan(c)) {
    Serial.println("값을 읽어오지 못했습니다.");
    return;
  }
}