/*
  Read moisture sensor and send data over USB

  Reads an analog input pin connected to moisture sensor.
  Sends the data over USB.

*/

// These constants won't change. They're used to give names to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int spiderInPin = A1;  // Sensor connected to spider plant

int sensorValue = 0;  // value read from the pot
int spiderValue = 0;  // value read from the pot

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);
  spiderValue = analogRead(spiderInPin);
  // Print value to usb
  Serial.print("{catnip:")
  Serial.print(sensorValue);
  Serial.print(",spider:")
  Serial.print(spiderValue);
  Serial.println("}")
  delay(1000);
}
