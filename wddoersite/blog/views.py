# coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from models import Note, Category
from datetime import datetime


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
