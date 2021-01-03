from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import BlogModel


class ShowBlog(View):
    def get(self, request):
        blog_events = BlogModel.objects
        return render(request, 'blog/posts.html', {'blog_events': blog_events})


class SpecificPost(View):
    def get(self, request, post_id):
        post = get_object_or_404(BlogModel, pk=post_id)  # pk = primary key
        return render(request, 'blog/specific_post.html', {'post': post})

# Create your views here.
