from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
import math

# User profile model
class Profile(models.Model):
    # One-to-One relationship with the User model
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# Genre model for categorizing stories
class Genre(models.Model):
    # Category name for stories
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# Story model to store user-created stories
class Story(models.Model):
    # ForeignKey relationship with the Profile model for the author
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    genre = models.ManyToManyField(Genre, blank=False)  # A story can belong to multiple genres
    view = models.PositiveSmallIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def word_count(self):
        return len(self.content.split()) if self.content else 0  # Calculate the word count of the story content

    def __str__(self):
        return self.title or ''

    def genres(self):
        return self.genre.all()

    # Estimate reading time (250 words / 1 minute)
    def reading_time(self):
        return f"{math.ceil(self.word_count / 250)} min"

# Like model to represent user likes on stories
class Like(models.Model):
    # ForeignKey relationship with the Profile model for the user and the Story model for the story
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

# Comment model for user comments on stories
class Comment(models.Model):
    # ForeignKey relationship with the Profile model for the user and the Story model for the story
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
