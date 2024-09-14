from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('trainers/', views.list_trainers, name="trainers")
    path("register/member/", views.register_member, name="register_member"),
    # path("ludic/", views.test, name="Ludic test")
    path("weight/record/", views.dailyweightrecord, name="daily_weight_record"),
    path("showrecords/", views.member_select_view, name="show_member_records"),
    path("showrecords/member/", views.weight_records_view, name='weight_records'),
]