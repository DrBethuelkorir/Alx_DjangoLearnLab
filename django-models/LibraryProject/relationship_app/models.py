from django.db import models

class Author(models.Model):  # Capital M
    name = models.CharField(max_length=200)

class Book(models.Model):  # Capital M
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # models.CASCADE

class Library(models.Model):  # Capital M
    name = models.CharField(max_length=200)  # models.CharField with max_length
    books = models.ManyToManyField(Book)  # ManyToManyField

class Librarian(models.Model):  # Capital M
    name = models.CharField(max_length=200)
    library = models.OneToOneField(
        Library, 
        on_delete=models.CASCADE  # Required on_delete parameter
    )