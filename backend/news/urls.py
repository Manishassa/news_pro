from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListCreate.as_view(), name='news_list_create'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),
]


