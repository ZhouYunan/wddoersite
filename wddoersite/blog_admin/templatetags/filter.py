from django.template.defaulttags import register

__author__ = 'wddoer'

def get_value(dict, k):
    """
    https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
    """
    return dict[k]

register.filter('get_value', get_value)