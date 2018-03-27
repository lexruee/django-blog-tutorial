from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    resgistered = models.DateTimeField()

    def __str__(self):
        return '<User %s, %s />' % (self.first_name, self.last_name)

class Post(models.Model):
    author = models.ForeignKey(User) 
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return '<Post %s />' % self.title

class Comment(models.Model):
    author = models.ForeignKey(User) 
    pub_date = models.DateTimeField('date published')
    post = models.ForeignKey(Post) 
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return '<Comment %s />' % self.title


