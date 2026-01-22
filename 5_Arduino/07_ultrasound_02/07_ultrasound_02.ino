#define TRIG 9
#define ECHO 8


void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);

  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;

  Serial.print(distance);
  Serial.println("cm");
  delay(100);

  digitalWrite(13, LOW);
  digitalWrite(12, LOW);


  if (distance < 5) {
    Serial.println("물체가 가까워짐");
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
  }
  delay(500);
  
}
