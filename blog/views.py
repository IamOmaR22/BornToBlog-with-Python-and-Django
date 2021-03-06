from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
    paginate_by = 5  # Five Post Per Page



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5  # Two Post Per Page

    # Override This query method (Custom Filter Query)
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))  # We Get The username from the url
        return Post.objects.filter(author=user).order_by('-date_posted')  # Filter With user and order by date.



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



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'   # To The Home Page

    def test_func(self):
        post = self.get_object()   # Get The Exact Post That We Are Currently Updating.

        if self.request.user == post.author:  # Check The Current User Is The Author Of The Post.
            return True

        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
