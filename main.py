import time
import signal
import sys

from arduino import update_antenna_position  # Importing the function from your module

def signal_handler(sig, frame):
    print("Exiting the program.")
    sys.exit(0)

def main():
    # Set up signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    COM_port = 'COM3'  # Example COM port

    try:
        while True:
            update_antenna_position(COM_port)
            time.sleep(30)  # Wait for 1 second
    except KeyboardInterrupt:
        print("Exiting the program.")

if __name__ == "__main__":
    main()
