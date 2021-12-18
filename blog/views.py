from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm

# Create your views here.
# def blog(request):
#     return render(request, 'blog.html', {})

class Blog(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'