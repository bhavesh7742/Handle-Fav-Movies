from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
    
