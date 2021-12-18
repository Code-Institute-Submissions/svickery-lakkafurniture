from django.contrib import admin
from django.urls import path
from .views import Blog, BlogDetail, AddPost

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', Blog.as_view(), name="blog"),
    path('article/<int:pk>', BlogDetail.as_view(), name='blog-article'),
    path('add_post/', AddPost.as_view(), name="add_post"),
]