# relationship_app/admin.py

from django.contrib import admin
from .models import Book, Library  # Import your models here

# Register your models to make them accessible through the admin interface
admin.site.register(Book)
admin.site.register(Library)

