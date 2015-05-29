from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.WddoerAdminView.as_view(), name='wddoer_admin_index'),
    url(r'^category/$', views.CategoryAdminView.as_view(), name='category_admin_index'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category/update/(?P<pk>\d+)/$', views.CategoryUpdateView.as_view(), name='category_update'),
]
