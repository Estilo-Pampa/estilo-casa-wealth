# Python code for reading sensor data from Arduino

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def read_sensor_data():
    ser.flushInput()
    data = ser.readline().decode().rstrip().split('\t')
    temperature = float(data[0].split(':')[1].strip())
    humidity = float(data[1].split(':')[1].strip())
    pressure = float(data[2].split(':')[1].strip())
    return temperature, humidity, pressure
