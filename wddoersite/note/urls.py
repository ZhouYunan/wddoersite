from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'note/$', views.NoteIndexView.as_view(), name='indexNote'),

]
