from django.contrib import admin

# Register your models here.
from .models import Title, Post

admin.site.register(Title)
admin.site.register(Post)