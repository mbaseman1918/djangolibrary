from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=250, default="Title not specified")
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default="Author not specified")

    def __str__(self):
        return self.title

class Availability(models.Model):
    user = models.CharField(max_length=250, default='Currently Available')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateField(default=date.today())

    def __str__(self):
        return self.book
