# coding:utf-8
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, FormView
from wddoersite.blog.models import Note, Category
from forms import CategoryCreateForm, NoteCreateForm, UserCreateForm, IdeaCreateForm
from django.core.urlresolvers import reverse, reverse_lazy
from wddoersite.iadmin.models import User
from wddoersite.idea.models import Idea


class WddoerAdminView(TemplateView):
    template_name = 'iadmin/blog_admin_index.html'

    def get_context_data(self, **kwargs):
        context = super(WddoerAdminView, self).get_context_data(**kwargs)
        context['amount_category'] = Category.objects.all().count()
        context['amount_category_displayed'] = Category.objects.exclude(is_displayed=False).count()
        context['amount_note'] = Note.objects.all().count()
        context['amount_note_displayed'] = Note.objects.exclude(is_displayed=False).count()
        context['amount_idea'] = Idea.objects.all().count()
        context['amount_idea_displayed'] = Idea.objects.filter(tag="DSBJ").exclude(is_displayed=False).count()
        context['amount_user'] = User.objects.all().count()
        context['amount_user_admin'] = User.objects.exclude(is_admin=False).count()
        return context


class CategoryAdminView(ListView):
    template_name = 'iadmin/category_admin_index.html'
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
    template_name = 'iadmin/category_create.html'
    form_class = CategoryCreateForm

    def get_success_url(self):
        return reverse('category_admin_index')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'is_displayed']
    template_name = 'iadmin/category_update.html'

    def get_success_url(self):
        return reverse('category_admin_index')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'iadmin/category_delete.html'
    success_url = reverse_lazy('category_admin_index')


class NoteAdminView(ListView):
    template_name = 'iadmin/note_admin_index.html'
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteAdminView, self).get_context_data(**kwargs)
        return context


class NoteCreateView(CreateView):
    template_name = 'iadmin/note_create.html'
    form_class = NoteCreateForm

    def get_success_url(self):
        return reverse('note_admin_index')


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'is_displayed', 'category', 'content']
    template_name = 'iadmin/note_update.html'

    def get_success_url(self):
        return reverse('note_admin_index')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'iadmin/note_delete.html'
    success_url = reverse_lazy('note_admin_index')


class UserCreateView(CreateView):
    template_name = "iadmin/user_create.html"
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse('user_admin_index')


class UserLoginView(FormView):
    template_name = "iadmin/user_login.html"
    form_class = AuthenticationForm

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(UserLoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('wddoer_admin_index')


class UserLogoutView(FormView):
    template_name = "iadmin/user_logout.html"
    success_url = ""

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect("user_login")
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth.logout(self.request)
        return redirect("user_login")


class UserAdminView(ListView):
    template_name = "iadmin/user_admin_index.html"
    model = User


class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'password', 'is_active', 'is_admin']
    template_name = 'iadmin/user_update.html'

    def get_success_url(self):
        return reverse('user_admin_index')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'iadmin/user_delete.html'
    success_url = reverse_lazy('user_admin_index')


class IdeaAdminView(ListView):
    template_name = 'iadmin/idea_admin_index.html'
    model = Idea

    def get_context_data(self, **kwargs):
        context = super(IdeaAdminView, self).get_context_data(**kwargs)
        return context


class IdeaCreateView(CreateView):
    template_name = 'iadmin/idea_create.html'
    form_class = IdeaCreateForm

    def get_success_url(self):
        return reverse('idea_admin_index')


class IdeaUpdateView(UpdateView):
    model = Idea
    fields = ['tag', 'is_displayed', 'content']
    template_name = 'iadmin/idea_update.html'

    def get_success_url(self):
        return reverse('idea_admin_index')


class IdeaDeleteView(DeleteView):
    model = Idea
    template_name = 'iadmin/idea_delete.html'
    success_url = reverse_lazy('idea_admin_index')