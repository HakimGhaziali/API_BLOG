from django.shortcuts import render
from blogg.models import GeeksModel
from .serializers import PostSerializer , UserSerializer
from rest_framework import viewsets , serializers
from rest_framework import generics
from django.contrib.auth.models import User



class PostSerial(generics.ListCreateAPIView):
    
    queryset = GeeksModel.objects.all()
    serializer_class = PostSerializer
    template_name = 'profile_list.html'
    


class PostDetailSerial(generics.RetrieveUpdateAPIView):
    
    queryset = GeeksModel.objects.all()
    serializer_class = PostSerializer
    template_name = 'profile_list.html'
    

class UserlSerial(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetaillSerial(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
