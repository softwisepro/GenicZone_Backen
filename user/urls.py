from django.urls import path
from . import views

urlpatterns =[
    path('user/<str:username>', views.UserProfileView.as_view(), name='user')
]
