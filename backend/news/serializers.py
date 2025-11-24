from rest_framework import serializers
from .models import NewsPost

class NewsPostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = NewsPost
        fields = ['id', 'title', 'content', 'category', 'image', 'author', 'created_at', 'updated_at']
