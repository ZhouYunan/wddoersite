from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'about/$', views.AboutView.as_view(), name='about'),
    url(r'blog/$', views.NoteIndexView.as_view(), name='indexBlog'),
    url(r'^blog/note/(?P<pk>\d+)/$', views.NoteDetailView.as_view(), name='detailNote'),
    url(r'^blog/category/(?P<pk>\d+)/$', views.categoryIndex, name='indexCategory'),

]
