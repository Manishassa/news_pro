from django.db import models
from django.utils import timezone

class NewsPost(models.Model):
    CATEGORY_CHOICES = [
        ('politics','Politics'),
        ('sports','Sports'),
        ('technology','Technology'),
        ('entertainment','Entertainment'),
        ('other','Other'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    author = models.CharField(max_length=100, default='anonymous')
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
