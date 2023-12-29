import os
from flask import Flask, render_template, request
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import requests
import tensorflow as tf
import pandas as pd

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load Flask app
app = Flask(__name__)

# Load the model
os.chdir("./artifacts/model")
model = tensorflow.keras.models.load_model('keras_model.h5')
class_names = open("labels.txt", "r").readlines()
df = pd.read_csv("label.csv")

@app.route('/', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        apikey = request.form['apikey']
        url = request.form['url']

        if apikey == "1234":
            image_url = tf.keras.utils.get_file('image.jpg', origin=url, cache_dir="~/images")
            image = tf.keras.preprocessing.image.load_img(image_url, target_size=(224, 224))
            os.remove(image_url)
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            data[0] = normalized_image_array

            # Predicts the model
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index][2:].replace("\n", "")
            confidence_score = float(prediction[0][index])


            # Print the DataFrame to check its structure
            print(df)
            print(class_name)

            # Fetch min and max temperatures based on the class name
            temp_info = df[df.iloc[:, 1] == class_name].iloc[:, 2:4]
            print(temp_info)

            min_temp = temp_info.iloc[0, 0] if not temp_info.empty else 2
            max_temp = temp_info.iloc[0, 1] if not temp_info.empty else 4

            print("Min Temperature:", min_temp)
            print("Max Temperature:", max_temp)


            result = {
                "class_name": class_name,
                "confidence_score": confidence_score,
                "min_temp": min_temp,
                "max_temp": max_temp
            }

            return render_template('index.html', result=result)
        else:
            return render_template('index.html', error="Invalid API Key")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))