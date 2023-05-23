from rest_framework import serializers
from api.models import blogPost
from django.contrib.auth.models import User

class blogPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = blogPost
        fields = ['id', 'text', 'created', 'owner']

class UserSerializer(serializers.ModelSerializer):
    blogPost = serializers.PrimaryKeyRelatedField(many=True, queryset=blogPost.objects.all())

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            blogPost = [],
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'blogPost']

class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password']
