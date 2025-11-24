from django.contrib import admin
from .models import NewsPost

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_at')
    search_fields = ('title', 'author', 'content')
    list_filter = ('category',)
