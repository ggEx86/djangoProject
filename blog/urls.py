from django.urls import path
from . import views
from .views import PostListView, DetailPostView, CreatePostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('about/', views.about, name='blog_about'),
    path('post/new/', CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
]
