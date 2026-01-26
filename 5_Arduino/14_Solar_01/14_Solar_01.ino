const int PANEL_PIN = A0;
const int SW_PIN = 2;

long energy = 0;

const long SELL_ENERGY = 100;

const int MAX_CHARGE_RATE = 50;

void setup() {
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP);
}

void loop() {
  int raw = analogRead(PANEL_PIN);
  float voltage = (raw * 5.0) / 1023.0;

  int gain = (voltage / 5.0) * MAX_CHARGE_RATE;

  delay(1000);
  if (gain > 0) {
    energy += gain;
  }

  bool prev = HIGH;
  bool curr = digitalRead(SW_PIN);

  if (prev == HIGH && curr == LOW) {
    Serial.println("");
    Serial.println("에너지 판매");

    if (energy >= SELL_ENERGY) {
      energy -= SELL_ENERGY;
      Serial.println("");
      Serial.print("판매량 ");
      Serial.print(SELL_ENERGY);
      Serial.println(" V ");
      Serial.print("에너지 잔량");
      Serial.print(energy);
      Serial.println(" V ");
    } else {
      Serial.println("");
      Serial.println("판매 실패(에너지 부족)");
      Serial.print("현재 에너지 ");
      Serial.print(energy);
      Serial.println(" V ");

    prev = curr; // prev와 curr 을 재할당하는 코드 (이후에 쓰일 수 있기 때문!!)
    }
  }
  Serial.println("");
  Serial.print("전압 : ");
  Serial.print(voltage);
  Serial.println(" V ");
  Serial.print("적립량 : ");
  Serial.print(gain);
  Serial.println(" V ");
  Serial.print("잔여 에너지 : ");
  Serial.print(energy);
  Serial.println(" v ");

  delay(1000);
}
