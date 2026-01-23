#include <LiquidCrystal_I2C.h> 
#include <Servo.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);
Servo myServo;
int angle = 0;

void setup() {
  myServo.attach(10);
  myLCD.init();
  myLCD.backlight();
}

void loop() {
  int angleVal = analogRead(A0);
  angle = map(angleVal, 0, 1023, 0, 180);

  myServo.write(angle);

  myLCD.setCursor(0, 0);
  myLCD.print("Servo angle");
  myLCD.setCursor(0, 1);  
  myLCD.print(angle);
  delay(500);

  myLCD.clear();
}
