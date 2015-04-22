from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'blog/$', views.NoteIndexView.as_view(), name='indexNote'),
    url(r'^blog/(?P<pk>\d+)/$', views.NoteDetailView.as_view(), name='detailNote'),
    url(r'^blog/category/(?P<pk>\d+)/$', views.categoryIndex, name='indexCategory'),

]
