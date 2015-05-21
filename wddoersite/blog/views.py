from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView, MonthArchiveView, YearArchiveView
from models import Note, Category
from datetime import datetime


class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['visited_time'] = datetime.now()
        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class NoteIndexView(ListView):
    model = Note
    template_name = 'blog/index_blog.html'
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super(NoteIndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NoteDetailView(DetailView):
    model = Note
    template_name = 'blog/detail_blog.html'

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def categoryIndex(request, pk):
    cate = Category.objects.get(pk=pk)
    notes = cate.note_set.all()
    return render_to_response('blog/index_category.html',
        {
            'notes': notes,
            'category_name': cate.name,
            'categories': Category.objects.all()
        },
        context_instance=RequestContext(request)
    )
