# coding: utf-8

import django_filters
from wddoersite.idea.models import Idea


class IdeaFilter(django_filters.FilterSet):

    class Meta:
        model = Idea
        fields = {
            'content': ['icontains', ]
        }
