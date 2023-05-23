from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class ArticleCreateTest(APITestCase):
    # @classmethod
    # def setUpTestData(cls):
        
    # def setUp(self):
    #     self.user_data = {"email": "fsf@gmail.com", "password": "12345"}
    #     self.article_data = {"title": "some title", "content": "some content"}
    #     self.user = User.objects.create_user('fsf@gmail.com','12345')
    #     self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
