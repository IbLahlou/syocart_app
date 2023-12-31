import pandas as pd
import random
from datetime import datetime, timedelta

# Simulate data for a fridge with a random walk in temperature
num_rows = 1000
start_time = datetime.now()
time_values = [(start_time + timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S') for i in range(num_rows)]
humidity_values = []
temperature_values = []

# Generate temperatures with a random walk
current_temperature = random.uniform(2, 4)
for _ in range(num_rows):
    temperature = current_temperature + random.uniform(-1, 1)  # Random walk step
    current_temperature = temperature

    # Introduce an occasional trend in temperature (5% chance)
    if random.random() < 0.05:
        temperature = random.uniform(-10, 10)  # Random value between -10 and 10

    humidity = 47.0

    # Introduce a periodic trend in humidity (every 100 rows)
    if _ % 100 == 0:
        humidity += random.uniform(5, 10)  # Gradual increase

    # Add occasional noise (10% chance)
    if random.random() < 0.1:
        temperature += random.uniform(-1, 1)  # Add random noise between -1 and 1

    temperature = max(-10, min(temperature, 10))  # Ensure temperature stays between -10 and 10

    temperature_values.append(temperature)
    humidity_values.append(humidity)

# Create a DataFrame
data = {'Time': time_values, 'Humidity': humidity_values, 'Temperature': temperature_values}
df = pd.DataFrame(data)

# Save the simulated data to a CSV file
df.to_csv('out/sensor_data.csv', index=False)

print("Simulated data saved to simulated_fridge_data.csv:")
print(df)
