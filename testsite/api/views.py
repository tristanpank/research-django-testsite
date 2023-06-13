from django.shortcuts import render
from api.models import blogPost, filePost
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from api.serializers import UserSerializer, blogPostSerializer, CreateUserSerializer, FilePostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
import subprocess
from django.conf import settings
import moviepy.editor as moviepy

class BlogList(generics.ListCreateAPIView):
    
    serializer_class = blogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
      num_of_posts = self.request.query_params.get('num_of_posts')
      queryset = blogPost.objects.all().order_by('created') 
      if num_of_posts is not None:
          queryset = queryset[:int(num_of_posts)]
      return queryset


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
    
class FilePostViewSet(generics.ListCreateAPIView):
    serializer_class = FilePostSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
      print(str(settings.BASE_DIR)[:-9])
      num_of_videos = self.request.query_params.get('num_of_videos')
      queryset = filePost.objects.all()
      if num_of_videos is not None:
          queryset = queryset[:int(num_of_videos)]
      return queryset

    def perform_create(self, serializer):
        new_file = serializer.save(owner=self.request.user)
        if new_file.title[-3:] == "mov":
            image_path = str(settings.BASE_DIR)[:-9] + '\\media\\'
            mp4_name = new_file.title[:-3] + "mp4"
            mp4_url = str(new_file.file_url)[:-3] + "mp4"
            # print(mp4_url)
            clip = moviepy.VideoFileClip(image_path + str(new_file.file_url))
            clip.write_videofile(image_path + mp4_url)

            # ffmpeg_command = 'ffmpeg i ' + image_path + str(new_file.title) + ' ' + image_path + mp4_name
            # print(ffmpeg_command)
            # subprocess.call('ffmpeg i ' + image_path + str(new_file.title) + ' ' + image_path + mp4_name)
            new_file.title = mp4_name
            new_file.file_url = mp4_url
            new_file.save()

        

