from django.urls import path
from . import views

urlpatterns =[
    path('user/<int:id>', views.UserProfileView.as_view(), name='user')
]
