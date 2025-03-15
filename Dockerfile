# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_django_project.wsgi"]
