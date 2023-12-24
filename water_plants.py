import serial
import os
import json
import datetime
import time
from picamera import PiCamera


DURATION = 2
MOISTURE_FILE = '~/moisture_data.txt'

def main():
    # Save camera image
    camera = PiCamera()
    camera.capture(os.path.expanduser('~/plants.jpg'))
    camera.close()
    # Establish serial connection to read moisture data
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
    with open(os.path.expanduser(MOISTURE_FILE), 'a') as file:
        # Read and save data
        start_time = time.time()
        while (time.time() - start_time) < DURATION:
            line = json.loads(ser.readline().decode('utf-8').strip())
            try:
                spider = line['spider']
                catnip = lind['catnip']
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data_to_write = f'{timestamp},{spider},{catnip}\n'
                file.write(data_to_write)
                file.flush()
            except ValueError:
                pass  # Ignore non-numeric data

    # Close the serial connection
    ser.close()

if __name__ == '__main__':
    main()
