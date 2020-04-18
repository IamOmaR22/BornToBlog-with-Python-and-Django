from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post  # This will tell my ListView. What model to query and In order to create the list.
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # ['date_posted'] - oldest to newest and ['-date_posted'] - newest to oldest


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # <app>/<model>_<viewtype>.html




def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})