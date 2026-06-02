from django.urls import path, include
from blogging_app.views import dashboard

# app specific urlconf

app_name = "dashboard_app"

urlpatterns = [
    path("", dashboard.dashboard_view, name="dashboard"),
    path(
        "create_post/",
        dashboard.dashboard_create_post_view,
        name="dashboard_create_post",
    ),
    path(
        "submit_post/",
        dashboard.dashboard_submit_post_view,
        name="dashboard_submit_post",
    ),
    path(
        "edit_post/<slug:slug>/",
        dashboard.dashboard_update_post_view,
        name="dashboard_edit_post",
    ),
    path(
        "delete_post/<slug:slug>/",
        dashboard.dashboard_delete_post_view,
        name="dashboard_delete_post",
    ),
    path("posts/", dashboard.dashboard_posts_view, name="dashboard_posts"),
    path("upload_image/", dashboard.image_upload_view, name="image_upload"),
]
