# Use Python 3.10.0 image
FROM python:3.10.0-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY ./app /app/app

# Command to run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
