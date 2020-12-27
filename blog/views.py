from django.shortcuts import render
from django.views.generic.base import View
from .models import BlogModel


class ShowBlog(View):
    def get(self, request):
        blog_events = BlogModel.objects
        return render(request, 'blog/posts.html', {'blog_events': blog_events})

# Create your views here.
