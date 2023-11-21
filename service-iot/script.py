import serial
import pandas as pd
import time
import datetime


serial_port = 'COM8'  # Remplacez par le port série réel auquel votre Arduino est connecté
baud_rate = 115200

data = {'Time': [], 'Humidity': [], 'Temperature': []}

with serial.Serial(serial_port, baud_rate) as ser:
    for _ in range(100):  # Exécutez pendant 20 itérations
        line = ser.readline().decode('utf-8').strip()
        print(f'Ligne reçue : {line}')
        timestamp, humidity, temperature = map(float, line.split(','))
        data['Time'].append(timestamp)
        data['Humidity'].append(humidity)
        data['Temperature'].append(temperature)

df = pd.DataFrame(data)
df.to_csv('./out/sensor_data.csv', index=False)
