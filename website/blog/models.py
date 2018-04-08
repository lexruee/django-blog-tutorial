from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    pub_date = models.DateTimeField('date published')
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return '<Post %s />' % self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField('date published')
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return '<Comment %s />' % self.title


