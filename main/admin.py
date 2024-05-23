from django.contrib import admin
from .models import Movie, Comment
from moviepy.editor import VideoFileClip


class MovieAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Call the superclass save_model method to perform the default save functionality
        super().save_model(request, obj, form, change)

        # Check if movie_file is provided and duration is not already set
        if obj.movie_file and not obj.duration:
            # Get the file path
            file_path = obj.movie_file.path

            # Calculate the duration using moviepy
            video_clip = VideoFileClip(file_path)
            duration = video_clip.duration

            # Set the duration
            obj.duration = duration

            # Save the updated object
            obj.save()
admin.site.register(Movie, MovieAdmin)  
admin.site.register(Comment)
