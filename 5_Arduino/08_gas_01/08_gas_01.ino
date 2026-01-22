#define GAS_A0 A0
#define GAS_D0 8


void setup() {
  Serial.begin(9600);
  pinMode(GAS_A0, INPUT);
  pinMode(GAS_D0, INPUT);
  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");
  pinMode(13, OUTPUT);


}

void loop() {
  float sensorValue = analogRead(GAS_A0);
  int sensorDValue = digitalRead(GAS_D0);

  digitalWrite(13, LOW);

  Serial.print("아날로그 센서 입력 :");
  Serial.print(sensorValue);
  Serial.print("  | 디지털 센서 입력 : ");
  Serial.println(sensorDValue);
  
  if(sensorValue > 300){
    Serial.println("가스감지!!");
    digitalWrite(13, HIGH);
  }
  
  delay(1000);

}
