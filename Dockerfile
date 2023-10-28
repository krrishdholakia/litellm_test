# Use an official Python runtime as an image
FROM python:3.9
# The directory in the container
WORKDIR /app
# Copy requirements file into the container
COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# COPY the rest of your app's source code from your host to your image filesystem.
COPY . .
# Tell Docker that your container will listen on the specified port at runtime
EXPOSE $PORT
# Run the app
CMD uvicorn main:app --host 0.0.0.0 --port $PORT