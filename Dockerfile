# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# If no secret key is specified, generate one automatically
ARG DJANGO_SECRET_KEY
RUN if [ -z "$DJANGO_SECRET_KEY" ]; then \
    DJANGO_SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"); \
    fi
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Django_img.wsgi:application"]
