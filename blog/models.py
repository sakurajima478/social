from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-publish_date']
    
    def __str__(self):
        return self.author.username
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()
        

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username
    