# relationship_app/views.py
from django.shortcuts import render
from .models import Book  # Ensure the correct model is imported

def list_books(request):
    books = Book.objects.all()  # Fetch all book instances
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Correct template path
