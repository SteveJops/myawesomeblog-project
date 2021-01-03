from django.db import models


class BlogModel(models.Model):
    blog_title = models.CharField(max_length=300)
    blog_date = models.DateTimeField(auto_now=False)
    blog_text = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')

    def get_summary(self):
        return self.blog_text[:70]

    def __str__(self):
        return self.blog_title
