# Python code for connecting to and querying the MySQL database

import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='smart_home'
        )
        self.cursor = self.connection.cursor()

    def insert_sensor_data(self, temperature, humidity, pressure):
        query = 'INSERT
