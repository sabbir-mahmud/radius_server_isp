# imports
from django.shortcuts import redirect


def owner_roles(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.owner:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('client:clients')
        else:
            return redirect('/')
    return wrapper_func