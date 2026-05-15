from django.urls import path
from blogging_app.views import public

# app specific urlconf

app_name = "blogging_app"

urlpatterns = [
    path("", public.home, name="home"),
    path("blogpost/<slug:slug>/", public.post_detail_view, name="post"),
]
