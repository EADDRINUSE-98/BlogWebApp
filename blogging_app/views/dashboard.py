from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


# Create your dashboard views here.


# def staff_required(view_function, *args):
#     """returns a decorator"""
#
#     def staff_check(user):
#         """
#         Takes a user object. Then:
#         # - checks is the user is authenticated.
#         - then, checks user has staff permission.
#         """
#         # if not user.is_authenticated:
#         #     return False
#         if not user.is_staff:
#             raise PermissionDenied
#         return True
#
#     decorator = login_required(next=args[0])(user_passes_test(staff_check)(view_function))
#     return decorator


def staff_check(user):
    """
    Takes a user object. Then:
    - then, checks user has staff permission.
    """
    if not user.is_staff:
        raise PermissionDenied
    return True


@login_required()
@user_passes_test(staff_check)
def dashboard_view(request):
    return HttpResponse("This will be Dashboard")
