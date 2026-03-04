#define TRIG_PIN 14
#define ECHO_PIN 27
#define BUZZER   4
#define LED_BLUE 2

long duration;
float distance;

void setup() {
  Serial.begin(115200);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);

  digitalWrite(BUZZER, LOW);
  digitalWrite(LED_BLUE, LOW);
}

float getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);

  distance = duration * 0.034 / 2;
  return distance;
}
 // distance
void loop() {

  float d = getDistance();

  Serial.print("Distance: ");
  Serial.print(d);
  Serial.println(" cm");

  // Logic
  if (d < 20) {
    digitalWrite(LED_BLUE, HIGH);
    digitalWrite(BUZZER, HIGH);
  }
  else if (d < 50) {
    digitalWrite(LED_BLUE, HIGH);
    digitalWrite(BUZZER, LOW);
  }
  else {
    digitalWrite(LED_BLUE, LOW);
    digitalWrite(BUZZER, LOW);
  }

  delay(200);
}
