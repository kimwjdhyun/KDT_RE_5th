#include <SPI.h> 
#include <MFRC522.h> 

#define SS_PIN 10
#define RST_PIN 9
int RED_Pin = 7;
int BLUE_Pin = 6;
int BUZZER =5;

byte whiteCardUID[] = {62, 176, 186, 2};

MFRC522 myMFRC(SS_PIN, RST_PIN); 

void setup() {
  Serial.begin(9600);
  SPI.begin();
  myMFRC.PCD_Init();

  pinMode(RED_Pin,OUTPUT);
  pinMode(BLUE_Pin,OUTPUT);
  pinMode(BUZZER,OUTPUT);
  
  myMFRC.PCD_DumpVersionToSerial();  
  Serial.println("RFID 통신 준비 완료");
}

void loop() {

  if (!myMFRC.PICC_IsNewCardPresent()){
    return;
  }
  if (!myMFRC.PICC_ReadCardSerial()){
    return;

  Serial.print("card UID : ");
  }

  for (byte i = 0; i < myMFRC.uid.size; i++) {
    Serial.print(myMFRC.uid.uidByte[i]);
    Serial.print(" ");
  }
  Serial.println("");
  
  bool isWhiteCard = true;
  for (byte i = 0; i < myMFRC.uid.size; i++) {
    if (myMFRC.uid.uidByte[i] != whiteCardUID[i]) {
      isWhiteCard = false;
      break;
    }
  }
  
  if (isWhiteCard) {
    Serial.println("흰색 태그입니다");
    digitalWrite(BLUE_Pin, HIGH);
    tone(BUZZER, 1000, 200);
    delay(500);
    digitalWrite(BLUE_Pin, LOW);
  } else {
    Serial.println("다른 태그입니다");
    digitalWrite(RED_Pin, HIGH);
    tone(BUZZER, 1000, 200);
    delay(300);
    tone(BUZZER, 1000, 200);
    delay(300);
    
    digitalWrite(RED_Pin, LOW);
  }

  myMFRC.PICC_HaltA();
  myMFRC.PCD_StopCrypto1();
  
  delay(1000); 
  }