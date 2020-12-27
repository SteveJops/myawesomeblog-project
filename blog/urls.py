from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowBlog.as_view(), name="showblog"),
]
