from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=6, choices=GENDERS, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users_image', default="users_image/default_user_pic.png",blank=True, null=True)

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.TextField()
    book_pic = models.ImageField(upload_to='books_image', default="books_image/default_book_pic.png", blank=True, null=True)
    readers = models.ManyToManyField(User)

    def __str__(self):
        return self.name