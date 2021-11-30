from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField(max_length=200) #text portion of post
    art = models.ImageField(blank=True, upload_to='post_list') #image upload portion of post
    created_on = models.DateTimeField(default=timezone.now) #time stamp of when user submits button
    author = models.ForeignKey(User, on_delete=models.CASCADE) #author of the post


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #author of the post
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class UserProfile(models.Model): #foreign key relationship between UserProfile model and user model. For one user there is one profile, and for one profile there is one user (one ot one relationship in database)
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True) #blank = True field can be left blank, null = True can be left blank in database
    bio = models.TextField(max_length=500, blank = True, null = True)
    birth_date = models.DateField(null = True, blank= True)
    location = models.CharField(max_length=100, blank = True, null = True)
    picture = models.ImageField(upload_to = 'uploads/profile_pictures', default= 'uploads/profile_pictures/default.jpg', blank = True)
