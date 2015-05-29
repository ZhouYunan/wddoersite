from django.template.defaulttags import register

__author__ = 'wddoer'


def get_value(dict, k):
    """
    https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
    """
    # v = 0
    # try:
    #     v = dict[k]
    # except KeyError:
    #     v = 0
    # return v
    if k in dict:
        return dict.get(k)
    return ''

register.filter('get_value', get_value)