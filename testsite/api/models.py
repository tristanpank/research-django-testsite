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


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class filePost(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=80, blank=False, null=False)
    file_url = models.FileField(upload_to=upload_to, blank=True, null=True)