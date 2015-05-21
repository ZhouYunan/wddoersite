from django.conf.urls import url
from . import views
from django.views.generic import ArchiveIndexView
from wddoersite.blog.models import Note


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'about/$', views.AboutView.as_view(), name='about'),
    url(r'blog/$', views.BlogIndexView.as_view(), name='index_blog'),
    url(r'^blog/note/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='detail_blog'),
    url(r'^blog/category/(?P<pk>\d+)/$', views.categoryIndex, name='index_category'),
    # url(r'^archive/$', ArchiveIndexView.as_view(model=Note, date_field='created_date')),
]
