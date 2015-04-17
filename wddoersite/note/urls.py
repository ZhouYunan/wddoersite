from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'note/$', views.NoteIndexView.as_view(), name='indexNote'),
    url(r'^note/(?P<pk>\d+)/$', views.NoteDetailView.as_view(), name='detailNote'),
    url(r'^note/category/(?P<pk>\d+)/$', views.categoryIndex, name='indexCategory'),

]
