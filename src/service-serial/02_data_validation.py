import pandas as pd

# Read the CSV file
file_path = './out/sensor_data.csv'
df = pd.read_csv(file_path)

# Display the initial data
print("Initial Data:")
print(df)

# Validate and clean the data
try:
    # Convert 'Time' column to datetime format
    df['Time'] = pd.to_datetime(df['Time'], unit='s')

    # Check for missing values
    missing_values = df.isnull().sum()
    print("\nMissing Values:")
    print(missing_values)

    # Check for data format issues (you can add more validations as needed)
    invalid_data = df[(df['Humidity'] < 0) | (df['Temperature'] < -40) | (df['Temperature'] > 85)]
    print("\nInvalid Data:")
    print(invalid_data)

    # Drop rows with missing values or invalid data
    df = df.dropna()
    df = df[(df['Humidity'] >= 0) & (df['Temperature'] >= -40) & (df['Temperature'] <= 85)]

    # Display the cleaned data
    print("\nCleaned Data:")
    print(df)

    # Save the cleaned data to a new CSV file
    cleaned_file_path = './out/cleaned_sensor_data.csv'
    df.to_csv(cleaned_file_path, index=False)

    print(f"\nCleaned data saved to {cleaned_file_path}")
except Exception as e:
    print(f"Error during data validation: {e}")
