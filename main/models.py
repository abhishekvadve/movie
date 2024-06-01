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
    def __str__(self):
        return self.title
    
    
        


        


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