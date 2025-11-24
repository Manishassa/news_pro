from rest_framework import generics, permissions
from .models import NewsPost
from .serializers import NewsPostSerializer

class NewsListCreate(generics.ListCreateAPIView):
    queryset = NewsPost.objects.all().order_by('-created_at')
    serializer_class = NewsPostSerializer
    permission_classes = [permissions.AllowAny]  # allow read/create in dev; change to Auth if needed

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    permission_classes = [permissions.AllowAny]  # adjust in prod
