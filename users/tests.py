from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "email": "fsf@gmail.com",
            "password": "12345",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)


class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {"email": "fsf@gmail.com", "password": "12345"}
        self.user = User.objects.create_user("fsf@gmail.com", "12345")

    def test_login(self):
        response = self.client.post(reverse("token_obtain_pair"), self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        access_token = self.client.post(reverse("token_obtain_pair"), self.data).data[
            "access"
        ]
        response = self.client.get(
            path=reverse("user_view"), HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        # print(response.data)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], self.data["email"])
