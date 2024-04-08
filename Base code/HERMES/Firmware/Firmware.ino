#include <Tic.h>
#include <SoftwareSerial.h>

TicI2C tic1(14);
TicI2C tic2(15);

SoftwareSerial SerialGPS(8, 7);

float TargetAnglePan = 0;
float TargetAngleTilt = 0;
const float StepConstant = 127.2889;

void setup() {
  // Set the baud rate.
  Serial.begin(9600);
  while (!Serial);
  Wire.begin();
  delay(20);

  // Set the Tic's current position to 0
  tic1.haltAndSetPosition(0);
  tic2.haltAndSetPosition(0);

  // Exit safe start
  tic1.exitSafeStart();
  tic2.exitSafeStart();

  tic1.clearDriverError();
  tic2.clearDriverError();

  tic1.haltAndHold();
  tic2.haltAndHold();
}

void resetCommandTimeout() {
  tic1.resetCommandTimeout();
  tic2.resetCommandTimeout();
}

void delayWhileResettingCommandTimeout(uint32_t ms) {
  uint32_t start = millis();
  do {
    resetCommandTimeout();
  } while ((uint32_t)(millis() - start) <= ms);
}

void DelayPos1(int TargetPosition) {
  while (tic1.getCurrentPosition() != TargetPosition) {
    resetCommandTimeout();
  }
  tic1.haltAndHold();
}

void DelayPos2(int TargetPosition) {
  while (tic2.getCurrentPosition() != TargetPosition) {
    resetCommandTimeout();
  }
  tic2.haltAndHold();
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int commaIndex = input.indexOf(',');
    if (commaIndex != -1) {
      TargetAnglePan = input.substring(0, commaIndex).toFloat();
      TargetAngleTilt = input.substring(commaIndex + 1).toFloat();
      
      int targetPositionPan = -StepConstant * TargetAnglePan;
      int targetPositionTilt = StepConstant * TargetAngleTilt;
      
      tic1.setTargetPosition(targetPositionPan);
      DelayPos1(targetPositionPan);
      tic2.setTargetPosition(targetPositionTilt);
      DelayPos2(targetPositionPan);

      Serial.print("motor at target position: ");
      Serial.print(targetPositionPan);
      Serial.print(",");
      Serial.println(targetPositionTilt);
      Serial.println("\n");
    } else {
      // If command format is incorrect, send an error message
      delay(1000)
      Serial.println("Error: Invalid command format");
      Serial.printlin("\n");
    }
  }
}

