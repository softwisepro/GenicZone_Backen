from rest_framework.views import APIView
from .serializers import UserSerializer, UserPorfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt, datetime
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
                    serializer = UserSerializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response({ 'error' : 'passwords did not match'})
        
        except:
            return Response({ 'error' : 'something went wrong' }, status=status.HTTP_404_NOT_FOUND)
        



#########   User Profile Views #########

class UserProfileView(APIView):
    def get(self, request, id):
        try:
          profile = UserProfile.objects.get(id=id)
          profile = UserPorfileSerializer(profile)
          return Response(profile.data)
        except:
          return Response({ 'error' : 'Unable to get user'})