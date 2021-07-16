from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    writer = models.CharField(max_length=15, default='닉네임을 입력하세요')
    body = models.TextField()
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey (Post, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=50)


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserInformation(models.Model):
    user = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
        primary_key=True,
    )
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)