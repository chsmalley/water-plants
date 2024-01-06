import RPi.GPIO as GPIO
import time

DURATION = 1
WATER_LOGFILE = '~/water_log.txt'

def main():
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Define the GPIO pin
    pin = 18

    # Setup the pin as an output
    GPIO.setup(pin, GPIO.OUT)

    try:
        # Turn on the pin
        GPIO.output(pin, GPIO.HIGH)
            
        time.sleep(DURATION)
                                
        # Turn off the pin
        GPIO.output(pin, GPIO.LOW)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, cleanup GPIO settings
        GPIO.cleanup()

if __name__ == '__main__':
    main()
