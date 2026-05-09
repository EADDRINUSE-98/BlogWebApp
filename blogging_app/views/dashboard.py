from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

# from django.http import HttpResponse
from blogging_app import forms


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
