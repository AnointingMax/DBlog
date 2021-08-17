from django.urls import path
from .views import PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from . import views

urlpatterns = [
    path('', views.home, name="blogapp-home"),
    path('user/', views.user_details, name="user-detail"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('addcomment/<int:pk>/<int:post_id>',
         views.add_comment, name="add-comment"),
    path('like/<int:pk>/', views.LikePost, name="like-post"),
    path('comment/<int:post_id>/<int:pk>/',
         views.LikeComment, name="like-comment"),
]
