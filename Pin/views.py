from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pin
from .serializers import PostSerializer
from django.contrib.auth.models import User
from user.models import UserProfile

class PostView(APIView):
    def get(self, request):
        
      try:
        pin = Pin.objects.all()
        pins = PostSerializer(pin, many=True)
        return Response(pins.data)
      except:
        return Response({ 'error' : 'Unable to get feeds'})

class SinglePostView(APIView):
    def get(self, request, slug):
        
      try:
        pin = Pin.objects.get(slug=slug)
        pin = PostSerializer(pin)
        return Response(pin.data)
      except:
        return Response({ 'error' : 'Unable to get single pin'})


class UserPostView(APIView):
    def get(self, request, id):
        
      try:
        pin = Pin.objects.filter(postedBy=id)
        pins = PostSerializer(pin, many=True)
        num_posts = len(pin)
        if len(pins.data) > 0:
           return Response({ 'num_posts': num_posts , 'success' : pins.data })
        else:
           return Response({ 'NoPost' : 'No posts'})
      except:
        return Response({ 'error' : 'Unable to get posts'})


class CreatePostView(APIView):
    def post(self, request, id):
        
        
        image = request.FILES['image']
        content = request.data['content']
        title = request.data['title']

        try:
          try:
            user = User.objects.get(id=id)

            if(user is not None):
                profile = UserProfile.objects.get(user=id)

                pin = Pin(title=title, content=content, image=image, postedBy=user, postedByProfile=profile)
                pin.save()

                return Response({ 'success' : 'posted' })
              
            else:
                return Response({ 'error' : 'something went wrong in creating profile'})
          except:
            return Response({ 'error' : 'No user'})
        except:
          return Response({ 'error' : 'Unable to get user'})