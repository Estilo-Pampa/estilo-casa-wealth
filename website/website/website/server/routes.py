# Python code for handling routes and retrieving sensor data

from flask import jsonify
from app import app
from sensors import read_sensor_data

@app.route('/data')
def get_data():
    temperature, humidity, pressure = read_sensor_data()
    return jsonify({'temperature': temperature, 'humidity': humidity, 'pressure': pressure})
