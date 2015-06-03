# coding:utf-8
from functools import wraps
from django.http.response import Http404


def blog_admin_required(view_func):
    """
    Decorator for views that checks necessary conditions
    """
    @wraps(view_func)
    def _check(request, *args, **kwargs):
        if request.user.is_active:
            if not request.user.is_admin:
                raise Http404
            return view_func(request, *args, **kwargs)
        raise Http404
    return _check
