#include <DHT.h>
#define DHTPIN 3
#define DHTTYPE DHT11
#define GAS_A0 A0
#define GAS_D0 2
#define TRIG 4
#define ECHO 5
#define RED2 6
#define BUTTON 7
#define BUZZER 11

int RED = 8;
int BLUE = 9;
int GREEN = 10;

DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin();
  pinMode(GAS_A0, INPUT);
  pinMode(GAS_D0, INPUT);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(RED2, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(BUZZER, OUTPUT);
  Serial.println("Heater warming start");
  delay(1000);
  Serial.println("Heater warming complete, operation start");
  pinMode(RED, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(GREEN, OUTPUT);
}

void loop() {
  float h = myDHT.readHumidity();
  float c = myDHT.readTemperature();
  float f = myDHT.readTemperature(true);
  float sensorValue = analogRead(GAS_A0);
  int sensorDValue = digitalRead(GAS_D0);
  
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  
  long duration = pulseIn(ECHO, HIGH);
  float distance = duration * 0.034 / 2;
  
  int buttonState = digitalRead(BUTTON);
  
  digitalWrite(RED, LOW);
  digitalWrite(BLUE, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(RED2, LOW);
  noTone(BUZZER);
  
  if (isnan(h) || isnan(c) || isnan(f)) {
    Serial.println("Failed to read values.");
  }
  
  Serial.print("Analog Sensor Input: ");
  Serial.print(sensorValue);
  Serial.print("  | Digital Sensor Input: ");
  Serial.println(sensorDValue);
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" | Celsius Temperature: ");
  Serial.print(c);
  Serial.print(" | Fahrenheit Temperature: ");
  Serial.print(f);
  Serial.print(" | Distance: ");
  Serial.print(distance);
  Serial.print(" cm | Button: ");
  Serial.println(buttonState);
  
  if(sensorValue > 300){
    Serial.println("Gas Detected!!");
  }
  
  if(sensorValue < 200) {
    digitalWrite(GREEN, HIGH);
    Serial.println("Status: Safe (Green LED)");
  }
  else if(sensorValue >= 200 && sensorValue < 500) {
    digitalWrite(BLUE, HIGH);
    Serial.println("Status: Warning (Blue LED)");
  }
  else {
    digitalWrite(RED, HIGH);
    Serial.println("Status: Danger (Red LED)");
    
    if(distance <= 5) {
      Serial.println(">>> Close proximity detected!");
      
      if(buttonState == LOW) {
        Serial.println(">>> Button Pressed - Buzzer ON!");
        digitalWrite(RED2, HIGH);
        tone(BUZZER, 1000);
        delay(500);
        digitalWrite(RED2, LOW);
        noTone(BUZZER);
        delay(500);
      }
      else {
        digitalWrite(RED2, HIGH);
        delay(100);
        digitalWrite(RED2, LOW);
        delay(100);
      }
    }
  }
  
  Serial.println("--------------------------------------");
  delay(500);
}