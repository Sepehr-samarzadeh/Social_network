from django.urls import path
from .views import PostView,PostListView, CommentView, LikeView

urlpatterns=[
    path('post/',PostView.as_view(),name='post'),
    path('post/<int:post_pk>/',PostView.as_view(),name='post'),
    path('posts-list/',PostListView.as_view(),name='posts-list'),
    path('post/<int:post_pk>/comments/', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/likes/', LikeView.as_view(), name='like'),
]