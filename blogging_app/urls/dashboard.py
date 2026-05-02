from django.urls import path, include
from blogging_app.views import dashboard

# app specific urlconf

app_name = "dashboard_app"

urlpatterns = [
    path("", dashboard.dashboard_view, name="dashboard"),
    # path("", include("django.contrib.auth.urls")),
]
