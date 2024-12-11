#include <107-Arduino-Servo-RP2040.h>

// Create a Servo object
static _107_::Servo thumb, pointer, middle, ring, pinky;

void setup() {
  Serial.begin(115200);
  while (!Serial) { }

  // Attach the servo to pin 2
  // Replace '2' with the GPIO pin number you’ve wired your servo to.
  thumb.attach(1);
  pointer.attach(0);
  middle.attach(4);
  ring.attach(3);
  pinky.attach(5);

  zero();

  Serial.println("Servo test started...");
}

char myData[50] = { 0 }, s1[10], s2[10], s3[10], s4[10], s5[10];

void loop() {
  zero();
  // byte n = Serial.available();
  // if (n != 0) {
    
  //   byte m = Serial.readBytesUntil('\n', myData, 50);
  //   myData[m] = '\0';  //null-byte
  //   float y1, y2, y3, y4, y5;
  //   // Serial.println(myData);
  //   if (sscanf(myData, "%[^','],%[^','],%[^','],%[^','],%s", s1, s2, s3, s4, s5) == 5) {
  //     y1 = atof(s1);
  //     y2 = atof(s2);
  //     y3 = atof(s3);
  //     y4 = atof(s4);
  //     y5 = atof(s5);

  //     Serial.print("float y1 = ");
  //     Serial.println(y1, 2);
  //     Serial.print("float y2 = ");
  //     Serial.println(y2, 2);
  //     Serial.print("float y3 = ");
  //     Serial.println(y3, 2);
  //     Serial.print("float y4 = ");
  //     Serial.println(y4, 2);
  //     Serial.print("float y5 = ");
  //     Serial.println(y5, 2);

  //     thumb.write(180 - y1 * 180);
  //     pointer.write(180 - y2 * 180);
  //     middle.write(180 - y3 * 180);
  //     ring.write(180 - y4 * 180);
  //     pinky.write(y5 * 180);
  //   } else Serial.println("error in input!");
  // }
}

void zero() {
  thumb.write(0);
  pointer.write(0);
  middle.write(0);
  ring.write(0);
  pinky.write(180);
}