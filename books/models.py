from django.db import models

# Create your models here.


class Books(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=30)
    author = models.CharField(max_length=30,blank=True,null=True)