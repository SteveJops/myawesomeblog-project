from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowBlog.as_view(), name="showblog"),
    path('<int:post_id>/', views.SpecificPost.as_view(), name='specific_post'),
]
