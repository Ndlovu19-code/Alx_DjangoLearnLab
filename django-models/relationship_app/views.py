from django.views.generic import DetailView
from .models import Library  # Import the Library model

class LibraryDetailView(DetailView):
    model = Library  # Specify the model for the view
    template_name = 'library_detail.html'  # Template to render
    context_object_name = 'library'  # Context object name in the template

