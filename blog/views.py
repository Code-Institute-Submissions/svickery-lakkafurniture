from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
# def blog(request):
#     return render(request, 'blog.html', {})

class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')