from django.dispatch import receiver
from django.db.models.signals import post_save
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
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='blog_images/user (1).png')

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()