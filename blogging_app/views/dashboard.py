from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from blogging_app import forms
from blogging_app.models import Post
from django.utils.text import slugify
from time import time

# Create your dashboard views here.


def staff_check(user):
    """
    Takes a user object and then checks user has staff permission.
    """
    if not user.is_staff:
        raise PermissionDenied
    return True


@login_required()
@user_passes_test(staff_check)
def dashboard_view(request):
    return render(request, "dashboard/home.html")


@login_required()
@user_passes_test(staff_check)
def dashboard_create_post_view(request):
    form = forms.CreatePostForms()
    context = {"form": form}
    return render(request, "dashboard/create_post.html", context)


@login_required()
@user_passes_test(staff_check)
def dashboard_submit_post_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Will create a custom 404 forbidden page.")
    try:
        post = Post(
            title=request.POST["title"],
            description=request.POST["description"],
            is_published=request.POST["is_published"],
            content=request.POST["content"],
        )

        slug = f"{slugify(request.POST['title'])}-{str(int(time()))}"

        post.slug = slug
        post.save()
        return redirect("blogging_app:post", slug=post.slug)
    except Exception as e:
        return HttpResponse(f"Exception: {e}")


@login_required
@user_passes_test(staff_check)
def dashboard_update_post_view(request):
    pass
