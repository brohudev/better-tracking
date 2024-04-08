#include <Tic.h>

TicI2C panMotor(14);
TicI2C tiltMotor(15); 
float TargetAnglePan = 0;
float TargetAngleTilt = 0;
const float StepConstant = 127.2889;

void setup() {
  panMotor.exitSafeStart();
  tiltMotor.exitSafeStart();
  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  // Check if serial data is available
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    
    int commaIndex = input.indexOf(',');
    if (commaIndex != -1) {
      //extract angle
      TargetAnglePan = input.substring(0, commaIndex).toFloat();
      TargetAngleTilt = input.substring(commaIndex + 1).toFloat();
      
      //calculate position
      int targetPositionPan = -StepConstant * TargetAnglePan;
      int targetPositionTilt = StepConstant * TargetAngleTilt;
      
      // give comand
      panMotor.setTargetPosition(targetPositionPan);
      tiltMotor.setTargetPosition(targetPositionTilt);
      
      // Wait until command is executed
      while (!isMotorAtPosition(panMotor) || !isMotorAtPosition(tiltMotor)) {}
    }
  }
}

// Helper method
bool isMotorAtPosition(TicI2C& motor) {
  int targetPosition = motor.getTargetPosition();
  int currentPosition = motor.getCurrentPosition();
  return (targetPosition == currentPosition);
}