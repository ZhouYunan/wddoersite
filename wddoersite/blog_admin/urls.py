from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.WddoerAdminView.as_view(), name='wddoer_admin_index'),
    url(r'^category/$', views.CategoryAdminView.as_view(), name='category_admin_index'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category/update/(?P<pk>\d+)/$', views.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^category/delete/(?P<pk>\d+)/$', views.CategoryDeleteView.as_view(), name='category_delete'),
    url(r'^note/$', views.NoteAdminView.as_view(), name='note_admin_index'),
    url(r'^note/create/$', views.NoteCreateView.as_view(), name='note_create'),
    url(r'^note/update/(?P<pk>\d+)/$', views.NoteUpdateView.as_view(), name='note_update'),
    url(r'^note/delete/(?P<pk>\d+)/$', views.NoteDeleteView.as_view(), name='note_delete'),
    url(r'^user/create/$', views.UserCreateView.as_view(), name='user_create'),
    url(r'^user/login/$', views.UserLoginView.as_view(), name='user_login'),
]
