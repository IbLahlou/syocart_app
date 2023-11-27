import os
from pathlib import Path
import logging

# Create the logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Set up the logging configuration
log_file = "logs/loggin_info.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [



    "requirements.txt",
    "README.md",
    #"deployement.yml",

    ## -------------------Service IOT--------------------
    "src/service-iot/script.py",
    "src/service-iot/Dockerfile",
    

    ## -------------------Service WEB---------------------
    "src/service-web/app.py",
    "src/service-web/Dockerfile",
    "src/service-web/static/css/style.css",
    "src/service-web/templates/index.html",
    "src/service-web/static/js/script.js",


    ## -------------------Service Data---------------------
    # local data

    ## -------------------Service Monitoring---------------------
    "src/service-monitoring/docker-compose.yml",
    "src/service-monitoring/prometheus.yml",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

# Log the completion of the file creation process
logging.info("File creation process completed")
