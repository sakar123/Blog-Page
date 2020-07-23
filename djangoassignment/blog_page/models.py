from django.db import models

# Create your models here.

class Blogs(models.Model):
    created_at = models.DateTimeField('Blog Created At:',  auto_now_add=True)
    updated_at = models.DateTimeField('Blog Updated At:', null=True, blank=True, auto_now=True)
    blog = models.TextField(max_length=15000)
    author = models.CharField(max_length=100)

    def __str__(self):
        to_return = self.author + "'s Blog Post"
        return to_return
