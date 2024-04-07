import serial
from azimuth_elevation_calculator import calculate_orientation
     

def update_antenna_position(COM_port):
    PanAngle, TiltAngle = calculate_orientation()

    if PanAngle is not None and TiltAngle is not None:  # Check if angles are calculated successfully
        Command = f"{PanAngle},{TiltAngle}"

        try:
            SerialPort = serial.Serial(port=COM_port, baudrate=9600, timeout=0.1)
            SerialPort.write(Command.encode())
            SerialPort.close()  # Close the serial port after sending the command
        except serial.SerialException as e:
            print(f"Error opening or writing to serial port: {e}")
    else:
        print("Error: Unable to calculate antenna angles.")