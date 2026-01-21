int button = 2;


void setup() {
  Serial.begin(9600);
  pinMode(button, INPUT_PULLUP);
}

void loop() {
  int buttonstate = digitalRead(button);
  Serial.println(buttonstate);
  delay(500);
}
