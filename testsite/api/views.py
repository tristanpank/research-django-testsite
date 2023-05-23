from django.shortcuts import render
from api.models import blogPost
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from api.serializers import UserSerializer, blogPostSerializer, CreateUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class BlogList(generics.ListCreateAPIView):
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateUser(generics.CreateAPIView):
    model = User
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)