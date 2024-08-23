# relationship_app/apps.py

from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # The default type for auto-incrementing primary keys
    name = 'relationship_app'  # The full Python path to the application

