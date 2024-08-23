# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library

# 1. Create Records

# Create a new author
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

# Create new books
book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1, publication_year=1997)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1, publication_year=1998)
book3 = Book.objects.create(title="1984", author=author2, publication_year=1949)

# Create a new library
library = Library.objects.create(name="Central Library", location="Main Street")

# Add books to the library
library.books.add(book1, book2, book3)

# 2. Retrieve Records

# Get all books
all_books = Book.objects.all()
print("All Books:")
for book in all_books:
    print(f"{book.title} by {book.author.name} (Published {book.publication_year})")

# Get all authors
all_authors = Author.objects.all()
print("\nAll Authors:")
for author in all_authors:
    print(author.name)

# Get books by a specific author
jk_rowling_books = Book.objects.filter(author=author1)
print("\nBooks by J.K. Rowling:")
for book in jk_rowling_books:
    print(book.title)

# Get a specific library and its books
library = Library.objects.get(name="Central Library")
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(f"{book.title} by {book.author.name}")

# 3. Update Records

# Update an author's name
author2.name = "George Orwell (Updated)"
author2.save()

# Update a book's title
book3.title = "Nineteen Eighty-Four"
book3.save()

print("\nUpdated Author and Book:")
print(f"Author: {author2.name}")
print(f"Book: {book3.title}")

# 4. Delete Records

# Delete a book
book_to_delete = Book.objects.get(title="Harry Potter and the Chamber of Secrets")
book_to_delete.delete()

print("\nAfter Deletion:")
remaining_books = Book.objects.all()
for book in remaining_books:
    print(f"{book.title} by {book.author.name}")

# 5. Advanced Queries

# Get books published after 1950
recent_books = Book.objects.filter(publication_year__gt=1950)
print("\nBooks Published After 1950:")
for book in recent_books:
    print(f"{book.title} (Published {book.publication_year})")

# Get libraries that have books written by a specific author
libraries_with_jk_rowling_books = Library.objects.filter(books__author=author1).distinct()
print("\nLibraries with Books by J.K. Rowling:")
for lib in libraries_with_jk_rowling_books:
    print(lib.name)
