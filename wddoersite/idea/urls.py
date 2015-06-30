from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IdeaIndexView.as_view(), name="idea_index"),
    # url(r'^(?P<pk>\d+)/$', views.IdeaDetailView.as_view(), name="idea_detail"),
    url(r'^filter/$', views.IdeaFilterView.as_view(), name="idea_filter"),
]