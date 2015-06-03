# coding:utf-8
from django.http import Http404
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, FormView
from wddoersite.blog.models import Note, Category
from forms import CategoryCreateForm, NoteCreateForm, UserCreateForm, UserLoginForm
from django.core.urlresolvers import reverse, reverse_lazy


class WddoerAdminView(TemplateView):
    template_name = 'blog_admin/blog_admin_index.html'

    def get_context_data(self, **kwargs):
        context = super(WddoerAdminView, self).get_context_data(**kwargs)
        context['amount_category'] = Category.objects.all().count()
        context['amount_note'] = Note.objects.all().count()
        return context


class CategoryAdminView(ListView):
    template_name = 'blog_admin/category_admin_index.html'
    model = Category        #不要用queryset = Category.objects.all(),否则会导致http://code.google.com/p/django-endless-pagination/issues/detail?id=22

    def get_context_data(self, **kwargs):
        context = super(CategoryAdminView, self).get_context_data(**kwargs)

        categories = Category.objects.all()
        notes_of_category = {}

        for cate in categories:         #接上一个注释，不能用self.queryset代替categories
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


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'blog_admin/category_delete.html'
    success_url = reverse_lazy('category_admin_index')


class NoteAdminView(ListView):
    template_name = 'blog_admin/note_admin_index.html'
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteAdminView, self).get_context_data(**kwargs)
        return context


class NoteCreateView(CreateView):
    template_name = 'blog_admin/note_create.html'
    form_class = NoteCreateForm

    def get_success_url(self):
        return reverse('note_admin_index')


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'is_displayed', 'category', 'content']
    template_name = 'blog_admin/note_update.html'

    def get_success_url(self):
        return reverse('note_admin_index')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'blog_admin/note_delete.html'
    success_url = reverse_lazy('note_admin_index')


class UserCreateView(CreateView):
    template_name = "blog_admin/user_create.html"
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse('user_login')


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = "blog_admin/user_login.html"

    def get_success_url(self):
        return reverse('wddoer_admin_index')

