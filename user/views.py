from rest_framework.views import APIView
from .serializers import UserSerializer, UserPorfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile

class RegisterView(APIView):
    def post(self, request):

        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        v_password = request.data['v_password']

        try:
            if password == v_password:
                if len(password) < 6:
                    return Response({ 'error' : 'Password should be at least 6 characters'})
            
                if User.objects.filter(email=email).exists():
                    return Response({ 'error' : 'Email is taken' })
                
                elif User.objects.filter(username=username).exists():
                    return Response({ 'error' : 'username is taken, try another' })
                
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    user = User.objects.get(id=user.id)
            
                    if user:
                        userprofile = UserProfile(user=user, first_name='', last_name='', username=username, profile_image='')
                        userprofile.save()
                    else:
                        return Response({ 'error' : 'something went wrong in creating profile'})

                    return Response({ 'success' : 'Account Created'})
            
            return Response({ 'error' : 'passwords did not match'})
        
        except:
            return Response({ 'error' : 'something went wrong' }, status=status.HTTP_404_NOT_FOUND)
        

        
class LoginView(APIView):
  def post(self, request, format=None):
    
    username = request.data['username']
    password = request.data['password']
    
    try:
      user = auth.authenticate(username=username, password=password)
    
      if user is not None:
        auth.login(request, user)

        user_profile = UserProfile.objects.get(user=user)
        serialiser = UserPorfileSerializer(user_profile)

        return Response({ 'success' : 'Login successful', 'user': serialiser.data })
      else:
        return Response({ 'error' : 'Either username or Password is not correc'})
    
    except:
      return Response({ 'error': 'Something went wrong when logging in'})

# this is the logout API

class LogoutView(APIView):
  def post(self, request, format=None):

    try:
      auth.logout(request)
      return Response({ 'success' : 'Loged out success' })
    except:
      return Response({ 'error' : 'Something went wrong when logging out' })
  
  
# this is the delete API
class DeleteView(APIView):
  def delete(self, request, format=None):
    user = self.request.user
    
    try:
      user = User.objects.filter(id=user.id).delete()
      return Response({ "success" : "Account was deleted successful" })
    except:
      return Response({ 'error' : 'Something Went wrong when deleting your account' })



#########   User Profile Views #########

class UserProfileView(APIView):
    def get(self, request, username):
        try:
          try:
            profile = UserProfile.objects.get(username=username)
            profile = UserPorfileSerializer(profile)
            return Response(profile.data)
          except:
            return Response({ 'error' : 'No user'})
        except:
          return Response({ 'error' : 'Unable to get user'})
        

        
class EditProfileImage(APIView):
   def put(self, request, id, username):
      
      new_profile_image = request.FILES['profile_image']

      try:
          user_id = UserProfile.objects.get(user=id)

          if(user_id is not None):
            
            user = User.objects.get(username=username)

            if user:
              new_profile =UserProfile.objects.get(user=user)
              new_profile.profile_image = new_profile_image
              new_profile.save()

              profile = UserProfile.objects.get(username=username)
              profile = UserPorfileSerializer(profile)

              return Response({ 'success' : 'updated', 'new_profile': profile.data })
          return Response({ 'error' : 'something went wrong' })
      except:
        return Response({ 'error' : 'Unable to get user'})

        

class EditUserProfileView(APIView):
    def post(self, request, id, username):
        
        new_username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        new_bio = request.data['bio']

        try:
          try:
            user_id = UserProfile.objects.get(user=id)
            
            if(user_id is not None):

              profile_name = User.objects.get(username=username)

              if(profile_name is not None):
                
                new_user=User.objects.get(username=username)
                new_user.username = new_username
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()

                user = User.objects.get(username=new_username)
            
                if user:
                  new_profile = UserProfile.objects.get(user=user)
                  
                  new_profile.first_name= first_name
                  new_profile.last_name = last_name
                  new_profile.username = new_username
                  new_profile.bio = new_bio
                  new_profile.save()

                  profile = UserProfile.objects.get(username=username)
                  profile = UserPorfileSerializer(profile)

                  return Response({ 'success' : 'updated', 'new_profile': profile.data })
                else:
                  return Response({ 'error' : 'something went wrong in creating profile'})
                
              else:
                  return Response({ 'error' : 'something went wrong in creating profile'})
              
            else:
                return Response({ 'error' : 'something went wrong in creating profile'})
          except:
            return Response({ 'error' : 'No user'})
        except:
          return Response({ 'error' : 'Unable to get user'})