from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Omar Faruk',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 07, 2020'
    },
    {
        'author': 'Jannat Akter',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 08, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})