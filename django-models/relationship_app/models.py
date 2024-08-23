# relationship_app/models.py

from django.db import models

# Define the Author model (assuming an Author model is needed)
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Book model
class Book(models.Model):
    title = models.CharField(max_length=200)  # Field to store the book title
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey to link the book with its author
    publication_year = models.IntegerField()  # Field to store the year the book was published

    def __str__(self):
        return self.title

# Define the Library model
class Library(models.Model):
    name = models.CharField(max_length=100)  # Field to store the library name
    location = models.CharField(max_length=255)  # Field to store the library location
    books = models.ManyToManyField(Book)  # ManyToManyField to link libraries with books

    def __str__(self):
        return self.name
