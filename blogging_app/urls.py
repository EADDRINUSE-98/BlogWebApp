from django.urls import path
from . import views

# app specific urlconf

app_name = "blogging_app"

urlpatterns = [
    path("", views.home, name="home"),
]
