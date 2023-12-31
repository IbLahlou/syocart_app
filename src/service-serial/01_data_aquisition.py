import serial
import pandas as pd

serial_port = 'COM8'  # Replace with the actual serial port to which your Arduino is connected
baud_rate = 115200

data = {'Time': [], 'Humidity': [], 'Temperature': []}

n = int(input("Enter the number of iterations: "))

print("Entering the loop...")
try:
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        for _ in range(n):  # Execute for specified iterations
           
            line = ser.read_until(b'\n').decode('utf-8').strip()
            print(f'Received line: {line}')
            
            # Ensure that the line contains the expected number of elements
            if ',' in line:
                timestamp, humidity, temperature = line.split(',')
                timestamp ,humidity, temperature = float(timestamp),float(humidity), float(temperature)
                data['Time'].append(timestamp)
                data['Humidity'].append(humidity)
                data['Temperature'].append(temperature)
except serial.SerialException as e:
    print(f"Serial Exception: {e}")

print("Exiting the loop.")

df = pd.DataFrame(data)
df.to_csv('./out/sensor_data.csv', index=False)
