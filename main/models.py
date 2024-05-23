from django.db import models
import os
from moviepy.editor import VideoFileClip, TextClip
from moviepy.editor import concatenate_videoclips
import random
import string
from django.contrib.auth.models import AbstractUser

LANGUAGES = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Tamil', 'Tamil'),
    ('Telugu', 'Telugu'),
    ('Malayalam', 'Malayalam'),
    ('Kannada', 'Kannada'),
    ('Bengali', 'Bengali'),
    ('Marathi', 'Marathi'),
]

RATINGS = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
    ('U', 'U'),
    ('UA', 'UA'),
    ('A', 'A'),
    ('S', 'S'),
    ('U/A', 'U/A'),
    ('A/A', 'A/A'),
]

GENRES = [
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Comedy', 'Comedy'),
    ('Crime', 'Crime'),
    ('Drama', 'Drama'),
    ('Fantasy', 'Fantasy'),
    ('Historical', 'Historical'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Romance', 'Romance'),
    ('Science Fiction', 'Science Fiction'),
    ('Thriller', 'Thriller'),
    ('Western', 'Western'),
]

class Movie(models.Model):
    title = models.CharField(max_length=100)
    logo = models.FileField(upload_to='logos/',default='media/1623408-t-9ec4d70dcf2b.webp')
    poster = models.FileField(upload_to='posters/',default='posters/default.jpg')
    trailer = models.FileField(upload_to='trailers/',default='trailers/default.mp4')
    language = models.CharField(max_length=100, choices=LANGUAGES)
    link = models.CharField(max_length=100)
    bio = models.TextField()
    genre = models.CharField(max_length=100, choices=GENRES, default='Action')
    duration = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField()
    movie_rating = models.CharField(max_length=100, choices=RATINGS, default='U')
    movie_file = models.FileField(upload_to='movies/',default='movies/default.mp4')
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.duration:  # Check if duration is not already set
            if self.movie_file:
                file_path = self.movie_file.path
                if os.path.exists(file_path):
                    duration = self.get_video_duration(file_path)
                    self.duration = duration
                    # Add title "Movie 1"
                    title = "Movie 1"
                    
                    # Generate random credits
                    credits = "Random Credits: "
                    for _ in range(5):  # Change 5 to the desired number of credits
                        credits += random.choice(string.ascii_letters)  # Add random letters
                    
                    # Create a text clip for title
                    title_clip = TextClip(title, fontsize=70, color='white')
                    title_clip = title_clip.set_duration(5)  # Duration of title clip (in seconds)
                    
                    # Create a text clip for credits
                    credits_clip = TextClip(credits, fontsize=30, color='white')
                    credits_clip = credits_clip.set_duration(10)  # Duration of credits clip (in seconds)
                    
                    # Concatenate title and credits clips with the movie clip
                    final_clip = concatenate_videoclips([title_clip, credits_clip, self.movie_file])
                    
                    # Save the final concatenated clip
                    
                    # Finally, call the save method of the parent class
        super().save(*args, **kwargs)
        

    def get_video_duration(self, file_path):
        try:
            clip = VideoFileClip(file_path)
            duration = clip.duration
            clip.close()
            return duration
        except Exception as e:
            print("Error getting video duration:", e)
            return None
        


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    

class User(AbstractUser):
    groups = None
    user_permissions = None
    pass