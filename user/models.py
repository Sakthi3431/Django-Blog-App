from django.db import models
from django.templatetags.static import static
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.username
