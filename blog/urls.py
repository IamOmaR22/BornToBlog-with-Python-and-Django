from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # post/1 or post/2 ... etc
    path('about/', views.about, name='blog-about'),
]