const int piezo_pin = 8;
const int btn = 2;

void setup() {
  Serial.begin(9600);
  pinMode(piezo_pin, OUTPUT);
  pinMode(btn, INPUT_PULLUP);
}

void loop() {
  int btnstate = digitalRead(btn);
  digitalWrite(piezo_pin, LOW);

  if (btnstate == LOW){
  Serial.println("btn:Piezo");
  digitalWrite((piezo_pin), HIGH);
  } else {
    Serial.println("btn:off");
  }
  delay(100);
}