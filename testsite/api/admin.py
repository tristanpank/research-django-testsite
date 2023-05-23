from django.contrib import admin
from api.models import blogPost, filePost

# Register your models here.
admin.site.register(blogPost)
admin.site.register(filePost)