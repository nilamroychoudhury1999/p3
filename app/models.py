from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    message =models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]+"..."