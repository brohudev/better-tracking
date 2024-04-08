import serial
import time

# Open serial port
ser = serial.Serial('COM3', 9600, timeout=1)

def send_command(pan_angle, tilt_angle):
    # Construct command string
    command = f"{pan_angle},{tilt_angle}\n"
    # Send command
    ser.write(command.encode())
    # Wait for response
    time.sleep(0.1)
    response = ser.readline().decode().strip()
    print(response)

try:
    # Send command to go left 30 degrees
    print("Sending command to go left 30 degrees")
    send_command(-30, 0)
    # Wait for motor to reach target position
    time.sleep(2)
    # Send command to go right 30 degrees
    print("Sending command to go right 30 degrees")
    send_command(30, 0)

finally:
    # Close serial port
    ser.close()
