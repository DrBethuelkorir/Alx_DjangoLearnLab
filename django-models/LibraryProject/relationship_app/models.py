from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name  # Added this line

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title  # Added this line

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name  # Added this line

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(
        Library, 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name  # Added this line