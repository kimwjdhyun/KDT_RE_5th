int DO = 2;
int RE = 3;
int MI = 4;
int FA = 5;
int SL = 6;

int piezo_pin = 8;

int tone_DO = 262;
int tone_RE = 294;
int tone_MI = 330;
int tone_FA = 349;
int tone_SOL = 392;

void setup() {
  pinMode(DO, INPUT_PULLUP);
  pinMode(RE, INPUT_PULLUP);
  pinMode(MI, INPUT_PULLUP);
  pinMode(FA, INPUT_PULLUP);
  pinMode(SL, INPUT_PULLUP);
  
  pinMode(piezo_pin, OUTPUT);
}

void loop() {

  if (digitalRead(DO) == LOW) {
    tone(piezo_pin, tone_DO);
  }

  else if (digitalRead(RE) == LOW) {
    tone(piezo_pin, tone_RE);
  }

  else if (digitalRead(MI) == LOW) {
    tone(piezo_pin, tone_MI);
  }

  else if (digitalRead(FA) == LOW) {
    tone(piezo_pin, tone_FA);
  }

  else if (digitalRead(SL) == LOW) {
    tone(piezo_pin, tone_SOL);
  }

  else {
    noTone(piezo_pin);
  }
}