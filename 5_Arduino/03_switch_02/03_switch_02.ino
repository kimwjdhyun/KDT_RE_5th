int switch1 = 12;
int switch2 = 11;
int ledgrn = 4;
int ledred = 3;

void setup(){
  Serial.begin(9600);
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  pinMode(ledgrn, OUTPUT);
  pinMode(ledred, OUTPUT);
}
void loop(){
  int SW1 = digitalRead(switch1);
  int SW2 = digitalRead(switch2);

  digitalWrite(ledgrn, LOW);
  digitalWrite(ledred, LOW);

  if(SW1 == LOW){
    Serial.println("Switch : GREEN");
    digitalWrite(ledgrn, HIGH);
  }
  if(SW2 == LOW){
    Serial.println("Switch : RED");
    digitalWrite(ledred, HIGH);
  }
  delay(100);
}
