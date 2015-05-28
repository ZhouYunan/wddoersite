# coding:utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView, YearArchiveView, CreateView
from models import Note, Category
from datetime import datetime
from wddoersite.blog.forms import CategoryCreateForm


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


class NoteYearArchiveView(YearArchiveView):
    template_name = "blog/blog_archive_year.html"
    queryset = Note.objects.filter(is_displayed=True, category__is_displayed=True)
    date_field = "created_date"
    make_object_list = True
    allow_future = True
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteYearArchiveView, self).get_context_data(**kwargs)
        context['amount_notes'] = self.queryset.count()
        return context


class WddoerAdminView(TemplateView):
    template_name = 'blog_admin/wddoer_admin_index.html'

    def get_context_data(self, **kwargs):
        context = super(WddoerAdminView, self).get_context_data(**kwargs)
        context['amount_category'] = Category.objects.all().count()
        context['amount_note'] = Note.objects.all().count()
        return context


class CategoryCreateView(CreateView):
    template_name = 'blog_admin/category_create.html'
    form_class = CategoryCreateForm
    success_url = ''

    def get_success_url(self):
        return self.success_url