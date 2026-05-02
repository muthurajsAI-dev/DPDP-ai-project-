# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your requirements file first (we will create this next)
COPY requirements.txt .

# Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code (app.py, middleware, etc.)
COPY . .

# Tell Docker which port the app runs on
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]