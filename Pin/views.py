from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pin
from .serializers import PostSerializer

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
