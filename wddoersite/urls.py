from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    # Examples:
    # url(r'^$', 'wddoersite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('wddoersite.blog.urls')),

    url(r'dashboard/', include('wddoersite.dashboard.urls')),

]
