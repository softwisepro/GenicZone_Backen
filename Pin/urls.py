from django.urls import path
from . import views

urlpatterns = [
    path('feeds', views.PostView.as_view(), name='pins'),
    path('feed/<str:slug>', views.SinglePostView.as_view(), name='single_pins'),
    path('user_posts/<int:id>', views.UserPostView.as_view(), name='user_posts'),
    path('create_post/<int:id>', views.CreatePostView.as_view(), name='add_posts'),
]