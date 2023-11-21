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
    "service-iot/script.py",
    #"service-iot/Dockerfile",
    

    ## -------------------Service WEB---------------------
    "service-web/app.py",
    #"service-web/Dockerfile",
    #"service-web/templates/css/style.css",
    #"service-web/templates/html/index.html",
    #"service-web/templates/js/script.js",


    ## -------------------Service Data---------------------
    # local data
    "out/data.csv",

    ## -------------------Service Monitoring---------------------
    #"service-monitoring/Dockerfile",

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
