from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.list_trainers, name="trainers")
]