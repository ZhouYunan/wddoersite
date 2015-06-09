# coding:utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView, YearArchiveView, CreateView
from django_filters.views import FilterView
from models import Note, Category
from datetime import datetime
from wddoersite.blog.filters import NoteFilter


class IndexView(TemplateView):
    template_name = 'blog/site_index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['visited_time'] = datetime.now()
        return context


class AboutView(TemplateView):
    template_name = 'blog/site_about.html'


class BlogIndexView(ListView):
    model = Note
    template_name = 'blog/blog_index.html'

    def get_context_data(self, **kwargs):
        context = super(BlogIndexView, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(is_displayed=True)
        context['notes'] = Note.objects.filter(is_displayed=True, category__is_displayed=True)

        return context


class BlogDetailView(DetailView):
    model = Note
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_displayed=True)
        return context


def categoryIndex(request, pk):
    cate = Category.objects.get(pk=pk)
    notes = cate.note_set.filter(is_displayed=True, category__is_displayed=True)
    return render_to_response('blog/category_index.html',
        {
            'notes': notes,
            'category_name': cate.name,
            'categories': Category.objects.filter(is_displayed=True)
        },
        context_instance=RequestContext(request)
    )


class NoteArchiveView(ListView):
    template_name = "blog/blog_archive.html"
    queryset = Note.objects.filter(is_displayed=True, category__is_displayed=True)
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteArchiveView, self).get_context_data(**kwargs)
        context['amount_notes'] = self.queryset.count()
        return context


class NoteFilterView(FilterView):
    template_name = "blog/blog_filter.html"
    filterset_class = NoteFilter
    queryset = Note.objects.filter(is_displayed=True, category__is_displayed=True).order_by("?")
