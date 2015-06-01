from django.conf.urls import url
from . import views
from decorators import blog_admin_required


urlpatterns = [
    url(r'^$', blog_admin_required(views.WddoerAdminView.as_view()), name='wddoer_admin_index'),
    url(r'^category/$', blog_admin_required(views.CategoryAdminView.as_view()), name='category_admin_index'),
    url(r'^category/create/$', blog_admin_required(views.CategoryCreateView.as_view()), name='category_create'),
    url(r'^category/update/(?P<pk>\d+)/$', blog_admin_required(views.CategoryUpdateView.as_view()), name='category_update'),
    url(r'^category/delete/(?P<pk>\d+)/$', blog_admin_required(views.CategoryDeleteView.as_view()), name='category_delete'),
    url(r'^note/$', blog_admin_required(views.NoteAdminView.as_view()), name='note_admin_index'),
    url(r'^note/create/$', blog_admin_required(views.NoteCreateView.as_view()), name='note_create'),
    url(r'^note/update/(?P<pk>\d+)/$', blog_admin_required(views.NoteUpdateView.as_view()), name='note_update'),
    url(r'^note/delete/(?P<pk>\d+)/$', blog_admin_required(views.NoteDeleteView.as_view()), name='note_delete'),
    url(r'^user/create/$', blog_admin_required(views.UserCreateView.as_view()), name='user_create'),
    url(r'^user/login/$', blog_admin_required(views.UserLoginView.as_view()), name='user_login'),
]
