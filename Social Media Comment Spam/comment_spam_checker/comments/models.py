# comments/models.py

from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length=100)
    profile_pic = models.URLField(default='https://via.placeholder.com/50')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=20, default='Safe')  # Spam/Suspicious/Safe

    def __str__(self):
        return self.username
