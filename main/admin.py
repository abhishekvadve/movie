from django.contrib import admin
from .models import Movie, Comment
from moviepy.editor import VideoFileClip


admin.site.register(Movie)  
admin.site.register(Comment)
