from django.contrib import admin
from .models import Post, UserProfile

admin.site.register(Post) #can view posts on admin page
admin.site.register(UserProfile)