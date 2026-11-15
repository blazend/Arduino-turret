#include <Servo.h>

// Create servo objects
Servo panServo;  // X-axis
Servo tiltServo; // Y-axis

// Define pins
const int PAN_PIN = 9;
const int TILT_PIN = 10;
const int LASER_PIN = 13; // Optional: Turns on the built-in LED/Laser when running

void setup() {
  // Your Python script uses 8000 baud, so we must match it exactly here
  Serial.begin(8000); 
  
  // Attach servos to pins
  panServo.attach(PAN_PIN);
  tiltServo.attach(TILT_PIN);
  
  // Optional: Set up laser pin
  pinMode(LASER_PIN, OUTPUT);
  digitalWrite(LASER_PIN, HIGH); // Turn laser on

  // Center the turret on startup
  panServo.write(90);
  tiltServo.write(90);
}

void loop() {
  // Check if both the X and Y bytes have arrived in the buffer
  if (Serial.available() >= 2) {
    // Read the incoming bytes
    int x_angle = Serial.read();
    int y_angle = Serial.read();
    
    // Constrain the angles between 0 and 180 to prevent servo strain
    x_angle = constrain(x_angle, 0, 180);
    y_angle = constrain(y_angle, 0, 180);
    
    // Move the servos
    panServo.write(x_angle);
    tiltServo.write(y_angle);
  }
}
