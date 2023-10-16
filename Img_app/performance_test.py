
import os
from locust import HttpUser, task, between
import json


"""
 To run the script : 
 USERNAME=your_username PASSWORD=your_password locust -f your_locust_file.py
 
 Ensure to avoid exposing sensitive information like username and password in bash history or logs. 
 In a real-world scenario, consider other secure methods to handle credentials, especially in a production environment.
"""

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = ""

    def on_start(self):
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASSWORD')

        if not username or not password:
            print("Username or password not set. Please set the USERNAME and PASSWORD environment variables.")
            return

        response = self.client.post("/api/token/", data={
            "username": username,
            "password": password
        })

        if response.status_code == 200:
            self.token = json.loads(response.text)['token']
        else:
            print(f"Failed to obtain token, status code {response.status_code}")
    
    @task
    def upload_image(self):
        if self.token:
            with open('test.jpg', 'rb') as f:
                headers = {'Authorization': f'Token {self.token}'}
                self.client.post("/images/", files={'image': f}, headers=headers)
        else:
            print("Token not available. Unable to upload image.")
    
    @task
    def get_images(self):
        if self.token:
            headers = {'Authorization': f'Token {self.token}'}
            self.client.get("/images/", headers=headers)
        else:
            print("Token not available. Unable to get images.")
