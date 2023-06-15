from django.urls import path
from . import views

urlpatterns = [
    path('feeds', views.PostView.as_view(), name='pins'),
    path('feed/<str:slug>', views.SinglePostView.as_view(), name='single_pins')
]