from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'wddoersite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^stock/', include('wddoersite.stock.urls')),

    url(r'^idea/', include('wddoersite.idea.urls')),

    url(r'', include('wddoersite.blog.urls')),

    url(r'^iadmin/', include('wddoersite.iadmin.urls')),

]
