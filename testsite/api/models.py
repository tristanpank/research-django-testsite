from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


class blogPost(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='blogPost', on_delete=models.CASCADE)
