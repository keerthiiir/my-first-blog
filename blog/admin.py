from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from .models import CVPost

admin.site.register(Post)
admin.site.register(CVPost)