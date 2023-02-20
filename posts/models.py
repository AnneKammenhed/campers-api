from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model for campers related to "owner", last post first
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    camping_title = models.CharField(max_length=255)
    camping_experience = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../samples/bike.jpg', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.camping_title}'
