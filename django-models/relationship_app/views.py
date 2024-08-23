# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library  # Import Library model

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Pass books to the template

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use
    template_name = 'relationship_app/library_detail.html'  # Specify the template to use
    context_object_name = 'library'  # Set the context object name for use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        return context
