#include <Tic.h>

TicI2C panMotor(14);  // Pan motor
TicI2C tiltMotor(15);  // Tilt motor

float TargetAnglePan = 0;
float TargetAngleTilt = 0;

const float StepConstant = 127.2889;

void setup() {
  panMotor.exitSafeStart();
  tiltMotor.exitSafeStart();
}

void loop() {
  // Retrieve current position of motors
  int currentPanPosition = panMotor.getCurrentPosition();
  int currentTiltPosition = tiltMotor.getCurrentPosition();

  // Convert target angles to target positions
  int targetPositionPan = -StepConstant * TargetAnglePan;
  int targetPositionTilt = StepConstant * TargetAngleTilt;

  // Set target positions for the motors
  panMotor.setTargetPosition(targetPositionPan);
  tiltMotor.setTargetPosition(targetPositionTilt);

  // Wait until motors reach the desired positions
  while (!isMotorAtPosition(panMotor) || !isMotorAtPosition(tiltMotor)) {  }
}

//helper method
bool isMotorAtPosition(TicI2C& motor) {
  int targetPosition = motor.getTargetPosition();
  int currentPosition = motor.getCurrentPosition();
  return (targetPosition == currentPosition);
}