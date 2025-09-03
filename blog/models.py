from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='blog_images/', blank=True, null=True, default='blog_images/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    file_url = models.URLField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
        
    @property
    def file_url(self):
        if self.file:                 # Safe: False when there is no file
            try:
                return self.file.url  # Works only if a file exists
            except ValueError:
                pass                  # In case a weird empty value slipped in
        return static('blog/assets/default.jpg')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    cmt_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"
    