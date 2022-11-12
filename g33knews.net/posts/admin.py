from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'Category', 'title', 'active']
admin.site.register(Post , PostAdmin)
