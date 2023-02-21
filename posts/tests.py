from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


# Create user anne and test to list all the posts
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='anne', password='cat')

    def test_list_posts(self):
        anne = User.objects.get(username='anne')
        Post.objects.create(owner=anne, camping_title='campervan')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
