# Use a specific Python base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app


# Install dependencies before copying code to leverage Docker caching
RUN pip install -r requirements.txt  && pip install .



# Create a non-root user and switch to it
RUN useradd -m ilduser
USER ilduser

# Mount the pip cache as a volume
VOLUME /home/myuser/.cache/pip

# Expose port 80
EXPOSE 80

# Specify Gunicorn settings (adjust workers and timeout as needed)

