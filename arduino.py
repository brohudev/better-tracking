# Standard Libraries
import os
import serial

import azimuth_elevation_calculator as aec


PanAngle, TiltAngle = 0, 0

SerialPort = serial.Serial(port=COM3, baudrate=9600, timeout=.1) 

PanAngle, TiltAngle = calculate_orientation()
Command = PanAngle + "," + TiltAngle

os.wait(1000)

SerialPort.write(Command.encode())