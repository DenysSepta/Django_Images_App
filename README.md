# Django_Images_App
A web application built with Django for uploading and managing images. The application supports different user tiers with varying levels of access and functionalities.
# Django Image Upload Application

A web application built with Django for uploading and managing images. The application supports different user tiers with varying levels of access and functionalities.

## Features

- **Image Upload**: Users can upload images in PNG or JPG format.
- **User Tiers**: Supports Basic, Premium, and Enterprise user tiers with additional features for higher tiers.
- **Admin Panel**: Django-admin based UI for administrative tasks and management.
- **Docker Support**: Includes Dockerfile and docker-compose.yml for easy containerization and deployment.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)

## Running the Application

### Using Python

1. Clone the repository:
   ```sh
   git clone https://github.com/DenysSepta/Django_Images_App
   cd Django_IMG


2. Install the dependencies:
    pip install -r requirements.txt

3. Apply migrations:

    python manage.py migrate

4. Run the development server:

    python manage.py runserver

5. Open a web browser and navigate to http://localhost:8000.


### Using Docker 

1. Clone the repository:

  

git clone <REPO-URL>
cd <PROJECT-DIRECTORY>

2. Build and run the Docker containers:

    docker-compose build
    docker-compose up

    Open a web browser and navigate to http://localhost:8000.

### Running Tests

1. Run the following command to execute the test suite:


python manage.py test

2. Run the following command to execute the performance test
    python USERNAME=your_username PASSWORD=your_password locust -f performance_test.py
