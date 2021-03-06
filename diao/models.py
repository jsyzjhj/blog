from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    create_time=models.DateTimeField()
    modify_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True)
    category=models.ForeignKey(Category,on_delete=True)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,on_delete=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url=reverse('diao:detial',kwargs={'pk':self.pk})
        return url
