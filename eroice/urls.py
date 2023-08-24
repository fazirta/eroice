# Import necessary modules
from django.contrib import admin  # Import the admin module
from django.urls import path       # Import the path function for URL routing
from . import views

# Define the URL patterns for the project
urlpatterns = [
    path('admin', admin.site.urls),  # URL pattern for the admin site
    path('', views.landing_view, name='landing'),  # Landing page URL
    path('login', views.login_view, name='login'),  # Login page URL
    path('logout', views.logout_view, name='logout'),  # Logout URL
    path('signup', views.register_view, name='signup'),  # User registration URL
    path('write', views.write_view, name='write'),  # URL for writing a new story
    path('home', views.home_view, name='home'),  # Home page URL
    path('story/<str:pk_story>', views.story_view),  # Story page URL with story ID parameter
    path('genre/<str:pk_genre>', views.genre_view),  # URL for stories of a specific genre with genre ID parameter
]

# Assign the custom view for handling 404 errors
handler404 = views.handle_not_found
handler500 = views.handle_server_error
