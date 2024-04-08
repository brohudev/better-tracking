import serial
import time

# Open serial port
ser = serial.Serial('COM3', 9600, timeout=1)

def send_command(pan_angle, tilt_angle):
    # Construct command string
    command = f"{pan_angle},{tilt_angle}\n"
    # Send command
    ser.write(command.encode())

try:
    # Send command to go left 30 degrees
    print("Sending command to go left 30 degrees")
    send_command(-30, 0)
    # Immediately switch to reading from serial
    while True:
        response = ser.readline().decode().strip()
        if response:
            print(response)
            break

    # Send command to go right 30 degrees
    print("Sending command to go right 30 degrees")
    send_command(30, 0)
    # Immediately switch to reading from serial
    while True:
        response = ser.readline().decode().strip()
        if response:
            print(response)
            break

finally:
    # Close serial port
    ser.close()
