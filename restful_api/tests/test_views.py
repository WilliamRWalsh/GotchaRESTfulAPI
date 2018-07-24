from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..serializers import UserSerializer


class CreateUserTest(APITestCase):
    def setUp(self):
        self.data = {'username': 'Starman', 'first_name': 'David', 'last_name': 'Bowie'}

    def test_list_user_post(self):
        url = reverse('user-list')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@gmail.com', 'dontuseadictionaryword')
        self.client.login(username='admin', password='dontuseadictionaryword')
        self.user = User.objects.create(username="Starman")

    def test_detail_user_delete(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="Starman")

    def test_list_user_get(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_user_get(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], UserSerializer(self.user).data['username'])


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('admin', 'admin@gmail.com', 'dontuseadictionaryword')
        self.client.login(username='admin', password='dontuseadictionaryword')
        self.user = User.objects.create(username="Starman", first_name="David", last_name="Bowie")
        self.data = UserSerializer(self.user).data
        self.data.update({'username': 'MajorTom'})

    def test_detail_user_put(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.data['username'])


class UnauthorizedTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="Starman", first_name="David", last_name="Bowie")
        self.data = UserSerializer(self.user).data
        self.data.update({'username': 'MajorTom'})

    def test_unauth_detail_user_put(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_detail_user_delete(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)