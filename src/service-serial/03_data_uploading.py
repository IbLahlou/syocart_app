from google.cloud import storage
import os

# Set the path to your service account key file
key_file_path = r"..\..\..\..\..\ASM-Project\projet_1\syocart.json"

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path

def upload_csv_to_bucket(project_id, bucket_name, source_file_path, destination_blob_name):
    try:
        # Create a client using the provided project ID and default credentials
        client = storage.Client(project=project_id)

        # Get the bucket and upload the CSV file to the specified folder
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # Upload the file
        blob.upload_from_filename(source_file_path)

        print(f"File {source_file_path} uploaded to {bucket_name}/{destination_blob_name}")

    except Exception as e:
        print(f"Error uploading file to Google Cloud Storage: {e}")

# Example usage
project_id = "syocart-iot-021"  # Replace with your actual project ID
bucket_name = "dht_sensors"
source_file_path = "out/sensor_data.csv"
destination_blob_name = "dht_serial.csv"  # Update the folder path as needed

upload_csv_to_bucket(project_id, bucket_name, source_file_path, destination_blob_name)
