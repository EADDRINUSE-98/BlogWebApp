from django.urls import path
from blogging_app.views import public

# app specific urlconf

app_name = "blogging_app"

urlpatterns = [
    path("", public.home, name="home"),
    path("blogpost/<int:pk>", public.PostDetailPage.as_view(), name="post"),
]
