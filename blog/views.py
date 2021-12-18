from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
# def blog(request):
#     return render(request, 'blog.html', {})

class blog(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'