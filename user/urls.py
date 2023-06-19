from django.urls import path
from . import views

urlpatterns =[
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    
    path('user/<str:username>', views.UserProfileView.as_view(), name='user'),
    path('edit/<int:id>/<str:username>', views.EditUserProfileView.as_view(), name='edit'),
    path('edit_profile_image/<int:id>/<str:username>', views.EditProfileImage.as_view(), name='edit')
]
