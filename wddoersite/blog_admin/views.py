# coding:utf-8
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from wddoersite.blog.models import Note, Category
from forms import CategoryCreateForm
from django.core.urlresolvers import reverse


class WddoerAdminView(TemplateView):
    template_name = 'blog_admin/blog_admin_index.html'

    def get_context_data(self, **kwargs):
        context = super(WddoerAdminView, self).get_context_data(**kwargs)
        context['amount_category'] = Category.objects.all().count()
        context['amount_note'] = Note.objects.all().count()
        return context


class CategoryAdminView(ListView):
    template_name = 'blog_admin/category_admin_index.html'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryAdminView, self).get_context_data(**kwargs)
        notes_of_category = {}
        for cate in self.queryset:
            key = cate.id
            notes_of_category[key] = Note.objects.filter(category_id=key).count()
        context['notes_of_category'] = notes_of_category
        return context


class CategoryCreateView(CreateView):
    template_name = 'blog_admin/category_create.html'
    form_class = CategoryCreateForm

    def get_success_url(self):
        return reverse('category_admin_index')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'is_displayed']
    template_name = 'blog_admin/category_update.html'

    def get_success_url(self):
        return reverse('category_admin_index')