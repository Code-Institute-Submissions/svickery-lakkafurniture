from django.contrib import admin
from django.urls import path
from .views import blog, BlogDetail

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', blog.as_view(), name="blog"),
    path('article/<int:pk>', BlogDetail.as_view(), name='blog-article'),
]