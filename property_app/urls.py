from django.urls import path

from . import views

app_name = "property_app"
urlpatterns = [
    path('', views.home, name='home'),  # Define a home view for the root URL
]