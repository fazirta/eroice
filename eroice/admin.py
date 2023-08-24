from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Profile, Genre, Story, Like, Comment

# Define a base admin class combining ImportExportModelAdmin and ModelAdmin
class CustomAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

# Register models with dynamically generated admin classes
def register_model_with_custom_admin(model):
    admin_class_name = f"{model.__name__}Admin"
    admin_attrs = {**vars(model)}  # Copy model attributes to admin attributes

    # Create a dynamic admin class using the type function
    admin_class = type(admin_class_name, (CustomAdmin,), admin_attrs)

    # Register the model with the dynamic admin class
    admin.site.register(model, admin_class)

# List of models to register
models_to_register = [Profile, Genre, Story, Like, Comment]

# Register each model with the custom admin class
for model in models_to_register:
    register_model_with_custom_admin(model)
