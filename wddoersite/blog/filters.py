# coding: utf-8

import django_filters
from wddoersite.blog.models import Note


class NoteFilter(django_filters.FilterSet):
    # title = django_filters.CharFilter(lookup_type="contains")

    class Meta:
        model = Note
        fields = {
            'title': ['icontains', ]
        }
