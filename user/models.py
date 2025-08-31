from django.db import models
from django.templatetags.static import static
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.username

class Registration(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=False)
    confirmpassword = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username