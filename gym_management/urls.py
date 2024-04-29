from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('trainers/', views.list_trainers, name="trainers")
    path("register/member/", views.register_member, name="register_member")
]