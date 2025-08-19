from django.db import models
from django.templatetags.static import static
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='blog_images/', blank=True, null=True, default='blog_images/default.jpg')
    
    def __str__(self):
        return self.title
