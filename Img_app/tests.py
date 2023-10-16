from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Image, AccountTier

class ImageTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create users for each plan
        self.basic_user = get_user_model().objects.create_user(username='basic', password='testpass', plan='Basic')
        self.premium_user = get_user_model().objects.create_user(username='premium', password='testpass', plan='Premium')
        self.enterprise_user = get_user_model().objects.create_user(username='enterprise', password='testpass', plan='Enterprise')

        self.client.login(username='basic', password='testpass')

        # TODO: Adjust this with the actual path of a test image file
        with open('path_to_test_image.jpg', 'rb') as img:
            response = self.client.post('/images/', {'image': img}, format='multipart')
            self.image_id = response.json()['id']

    def test_basic_user_images(self):
        response = self.client.get(f'/images/{self.image_id}/')
        self.assertIn('thumbnail_200', response.json())
        self.assertNotIn('thumbnail_400', response.json())
        self.assertNotIn('original', response.json())

    def test_premium_user_images(self):
        self.client.login(username='premium', password='testpass')
        response = self.client.get(f'/images/{self.image_id}/')
        self.assertIn('thumbnail_200', response.json())
        self.assertIn('thumbnail_400', response.json())
        self.assertIn('original', response.json())

    def test_enterprise_user_images(self):
        self.client.login(username='enterprise', password='testpass')
        response = self.client.get(f'/images/{self.image_id}/')
        self.assertIn('thumbnail_200', response.json())
        self.assertIn('thumbnail_400', response.json())
        self.assertIn('original', response.json())
        self.assertIn('expiring_link', response.json())

    def test_admin_create_tier(self):
        admin_user = get_user_model().objects.create_superuser(username='admin', password='testpass', email='admin@example.com')
        self.client.login(username='admin', password='testpass')
        
        # TODO: Modify the following with actual attributes and paths for creating a new tier
        data = {
            'name': 'Custom',
            'thumbnail_sizes': [150, 300],
            'original_link': True,
            'expiring_link': True
        }
        response = self.client.post('/account-tier/', data, format='json')
        self.assertEqual(response.status_code, 201)
