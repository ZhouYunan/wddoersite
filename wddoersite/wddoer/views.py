# coding:utf-8
import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from wddoersite import settings
from wddoersite.wddoer.forms import AuthenticationForm, RegistrationForm
from django.views.generic import FormView


class LoginView(FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'wddoer/login.html'

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):

        return super(LoginView, self).form_invalid(form)

    def get_success_url(self):
        next = self.request.POST.get('next', None)
        if next:
            return next

        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.request.POST.get(self.redirect_field_name, '')

        netloc = urlparse.urlparse(redirect_to)[1]
        if not redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL
        return redirect_to

    def get(self, request, *args, **kwargs):

        return super(LoginView, self).get(request, *args, **kwargs)

