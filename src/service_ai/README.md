# Flask Backend REST API Server for Teachable Machine Model
Current API Endpoint, hosting at: https://jellyfish-app-uq2na.ondigitalocean.app/

This repository contains the code for a custom API server that uses Keras models and is deployed using `Google Cloud Run` (or `Digital Ocean App Platform`). The purpose of this server is to provide a framework for building and deploying a RESTful API that can handle Keras models.

The server relies on the Flask framework, which is a lightweight and flexible framework for building web applications in Python. It provides the necessary infrastructure to handle HTTP requests and responses.

## API Endpoints
The following API endpoints are available:

- `POST /`: Accepts an API key and an image URL as parameters, sends a request to the Teachable Machine API, and returns the prediction results.

### Input Payload
The `POST /` endpoint expects the following parameters to be passed as query parameters in the URL:

- `apikey`: The API key generated for the Teachable Machine API. (for this example: it is `1234`)
- `url`: The URL of the image that you want to send for prediction.

### Output Format
The response from the `POST /` endpoint will be a JSON object with the following format:

```json
{
    "class_name": "?",
    "confidence_score": ?
}
```

The `confidence_score` field contains the predicted probabilities for each `class_name` in your Teachable Machine model.

## Getting Started
To get started with this server, follow the steps below:

1. Clone this repository to your local machine.
2. Make sure you have **Python version 3.8** installed.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Place your Teachable Machine model files (e.g., `.h5` or `.json` files) in the appropriate directory.
5. Open the `main.py` file and configure the necessary settings, such as the path to your model files and the desired port number.
6. Run the server by executing the command `python main.py`.

## Deployment
To deploy this server using Cloud Run, follow the steps below:

1. Set up a project on Google Cloud Platform and enable the Cloud Run API.
2. Build a Docker image of the server by running `docker build -t gcr.io/project-id/image-name .` in the project directory.
3. Push the Docker image to Google Container Registry by running `docker push gcr.io/project-id/image-name`.
4. Deploy the Docker image on Cloud Run by running `gcloud run deploy --image gcr.io/project-id/image-name --platform managed`.

Once the deployment is successful, you will receive a URL for your Cloud Run service, which can be used to access the API.
