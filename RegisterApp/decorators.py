from django.core.exceptions import PermissionDenied


def user_is_logged(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            raise PermissionDenied
        else:
            return function(request, *args, **kwargs)
    return wrap
