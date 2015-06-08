from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="site_index"),
    url(r'about/$', views.AboutView.as_view(), name="site_about"),
    url(r'blog/$', views.BlogIndexView.as_view(), name="blog_index"),
    url(r'^blog/note/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name="blog_detail"),
    url(r'^blog/category/(?P<pk>\d+)/$', views.categoryIndex, name="category_index"),
    url(r'^blog/archive/$', views.NoteArchiveView.as_view(), name="blog_archive"),
]
