from django.urls import path
import views

# app specific urlconf

app_name = "blogging_app"

urlpatterns = [
    path("", views.home, name="home"),
]
