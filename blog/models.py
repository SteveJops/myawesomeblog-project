from django.db import models


class BlogModel(models.Model):
    blog_title = models.CharField(max_length=300)
    blog_date = models.DateTimeField(auto_now=True)
    blog_text = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')
