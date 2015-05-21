from django.conf.urls import url
from . import views
from django.views.generic import ArchiveIndexView
from wddoersite.blog.models import Note


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="site_index"),
    url(r'about/$', views.AboutView.as_view(), name="site_about"),
    url(r'blog/$', views.BlogIndexView.as_view(), name="blog_index"),
    url(r'^blog/note/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name="blog_detail"),
    url(r'^blog/category/(?P<pk>\d+)/$', views.categoryIndex, name="category_index"),
    url(r'^archive/$', ArchiveIndexView.as_view(model=Note, date_field='created_date'), name="blog_archive"),
]
