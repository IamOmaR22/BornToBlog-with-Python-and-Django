from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # Form Valid Method. (override)
        form.instance.author = self.request.user  # Take That Instance and Set The Author = Current Logged In User.
        return super().form_valid(form)  # Run the form on parent class.


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()   # Get The Exact Post That We Are Currently Updating.

        if self.request.user == post.author:  # Check The Current User Is The Author Of The Post.
            return True

        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})