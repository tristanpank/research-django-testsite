from rest_framework import serializers
from api.models import blogPost, filePost
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

class FilePostSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    file_url = serializers.FileField(required=False)

    class Meta:
        model = filePost
        fields = ['id', 'owner', 'owner_id', 'title', 'file_url']