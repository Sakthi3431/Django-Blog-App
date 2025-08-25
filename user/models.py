from django.db import models
from django.templatetags.static import static
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