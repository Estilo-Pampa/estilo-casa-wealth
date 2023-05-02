// Code for Arduino Framework
// Include necessary libraries
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

// Define pins for BME280 sensor
#define BME_SDA 21
#define BME_SCL 22

// Initialize BME280 sensor object
Adafruit_BME280 bme;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize I2C communication for BME280
  Wire.begin(BME_SDA, BME_SCL);

  // Check if BME280 is detected
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  // Read data from BME280 sensor
  float temperature = bme.readTemperature();
  float humidity = bme.readHumidity();
  float pressure = bme.readPressure() / 100.0F;

  // Print data to serial monitor
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Pressure: ");
  Serial.print(pressure);
  Serial.println(" hPa");

  // Wait for 1 second before reading again
  delay(1000);
}
