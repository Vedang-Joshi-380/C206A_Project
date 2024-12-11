// /**************************************************************************************
//  * GLOBAL VARIABLES
//  **************************************************************************************/

// static _107_::Servo servo_0, servo_1, servo_2, servo_3;
// int micro; 

// /**************************************************************************************
//  * SETUP/LOOP
//  **************************************************************************************/

// void setup()
// {
//   Serial.begin(115200);
//   while (!Serial) { }

//   servo_0.attach(0);
// }

// void loop()
// {
//   for (micro = 400; micro <= 2500; micro++) {
//     servo_0.writeMicroseconds(micro);
//     delay(10);
//   }
// }

#include <107-Arduino-Servo-RP2040.h>

// Create a Servo object
static _107_::Servo thumb, pointer, middle, ring, pinky;

void setup() {
  Serial.begin(115200);
  while (!Serial) { }

  // Attach the servo to pin 2
  // Replace '2' with the GPIO pin number you’ve wired your servo to.
  thumb.attach(1);
  pointer.attach(2);
  middle.attach(3);
  ring.attach(4);
  pinky.attach(5);

  Serial.println("Servo test started...");
}

void loop() {
  // thumb.write(0);
  // pointer.write(0);
  // middle.write(0);
  // ring.write(0);
  // pinky.write(0);
  Serial.println("Sweep the servo from 0 to 180 degrees");
  for (int angle = 0; angle <= 120; angle++) {
    thumb.write(angle * 1.5);
    delay(30); // small delay for servo to reach position
  }
  for (int angle = 0; angle <= 120; angle++) {
    pointer.write(angle * 1.5);
    delay(30); // small delay for servo to reach position
  }
  for (int angle = 0; angle <= 120; angle++) {
    middle.write(angle * 1.5);
    delay(30); // small delay for servo to reach position
  }
  for (int angle = 0; angle <= 120; angle++) {
    ring.write(angle * 1.5);
    delay(30); // small delay for servo to reach position
  }
  for (int angle = 0; angle <= 120; angle++) {
    pinky.write(angle * 1.5);
    delay(30); // small delay for servo to reach position
  }
  // for (int micro = 400; micro <= 2500; micro++) {
  //   thumb.writeMicroseconds(micro);
  //   delay(10);
  // }
  Serial.println("Done");

  // Serial.println("Sweep the servo from 180 back to 0 degrees");
  // for (int angle = 180; angle >= 0; angle--) {
  //   thumb.write(angle);
  //   delay(150);
  // }
}
