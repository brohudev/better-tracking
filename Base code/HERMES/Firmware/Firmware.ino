#include <Tic.h>
#include <SoftwareSerial.h>

TicI2C tic1(14);
TicI2C tic2(15);

float TargetAnglePan = 0;
float TargetAngleTilt = 0;
const float StepConstant = 127.2889;

void setup() {
  // Set the baud rate.
  Serial.begin(9600);
    while (!Serial)
    ;
//  Serial.setTimeout(5);

//  SerialGPS.begin(9600);

  Wire.begin();
  delay(20);

  // Tells the Tic that it is OK to start driving the motor.  The
  // Tic's safe-start feature helps avoid unexpected, accidental
  // movement of the motor: if an error happens, the Tic will not
  // drive the motor again until it receives the Exit Safe Start
  // command.  The safe-start feature can be disbled in the Tic
  // Control Center.
  tic1.exitSafeStart();
  tic2.exitSafeStart();

  // Set the Tic's current position to 0, so that when we command
  // it to move later, it will move a predictable amount.
  tic1.haltAndSetPosition(0);
  tic2.haltAndSetPosition(0);

  tic1.clearDriverError();
  tic2.clearDriverError();
}

// Sends a "Reset command timeout" command to the Tic.  We must
// call this at least once per second, or else a command timeout
// error will happen.  The Tic's default command timeout period
// is 1000 ms, but it can be changed or disabled in the Tic
// Control Center.
void resetCommandTimeout()
{
  tic1.resetCommandTimeout();
  tic2.resetCommandTimeout();
}

// Delays for the specified number of milliseconds while
// resetting the Tic's command timeout so that its movement does
// not get interrupted by errors.
// void delayWhileResettingCommandTimeout(uint32_t ms)
// {
//   uint32_t start = millis();
//   do
//   {
//     resetCommandTimeout();
//   } while ((uint32_t)(millis() - start) <= ms);
// }

// Polls the Tic, waiting for it to reach the specified target
// position.  Note that if the Tic detects an error, the Tic will
// probably go into safe-start mode and never reach its target
// position, so this function will loop infinitely.  If that
// happens, you will need to reset your Arduino.
void DelayPos1(int TargetPosition) {
  while (tic1.getCurrentPosition() != TargetPosition) {
    resetCommandTimeout();
  }
}

void DelayPos2(int TargetPosition) {
  while (tic2.getCurrentPosition() != TargetPosition) {
    resetCommandTimeout();
  }
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
      tic1.setTargetPosition(targetPositionPan);
      DelayPos1(targetPositionPan);
      tic1.haltAndHold();

      tic2.setTargetPosition(targetPositionTilt);
      DelayPos2(targetPositionPan);
      tic2.haltAndHold();
    }
  }
}
