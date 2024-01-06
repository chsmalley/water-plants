import serial
import os
import json
import datetime
import time
from picamera import PiCamera


DURATION = 4
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
        catnip_values = []
        spider_values = []
        while (time.time() - start_time) < DURATION:
            try:
                line = ser.readline().decode('utf-8').strip().split(',')
            except UnicodeDecodeError:
                line = []
            try:
                if line:
                    catnip_values.append(line[0])
                    spider_values.append(line[1])
            except (ValueError, TypeError) as e:
                pass  # Ignore non-numeric data
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        spider = sorted(spider_values)[len(spider_values) // 2]
        catnip = sorted(catnip_values)[len(catnip_values) // 2]
        data_to_write = f'{timestamp},{spider},{catnip}\n'
        file.write(data_to_write)
        file.flush()

    # Close the serial connection
    ser.close()

if __name__ == '__main__':
    main()
