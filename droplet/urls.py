from django.urls import path
from . import views

urlpatterns = [
    path('get-droplet/', views.get_droplet),
    path('create-droplet/', views.create_droplet),
    path('delete-droplet/', views.delete_droplet),
]
