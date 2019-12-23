#include <NewPing.h>

#define TRIGGER_PIN1  9
#define TRIGGER_PIN2  6

#define ECHO_PIN1     10
#define ECHO_PIN2     7
#define MAX_DISTANCE 200

NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1, MAX_DISTANCE);
NewPing sonar2(TRIGGER_PIN2, ECHO_PIN2, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
}

void loop() {
  delay(50);
  int precisao = sonar1.ping_median(10);
  int precisao = sonar2.ping_median(10);
  Serial.print(sonar1.convert_cm(precisao));
  Serial.print(";");
  Serial.println(sonar2.convert_cm(precisao));
}
