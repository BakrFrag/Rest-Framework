from django.db import models
from django.contrib.auth.models import User;
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=128);
    content=models.TextField(blank=True,null=True);
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True);
    image=models.ImageField(upload_to="posts",blank=True,null=True);
    #shared_with=models.ManyToManyField(User,blank=True);
    updated=models.DateTimeField(auto_now=True);
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title