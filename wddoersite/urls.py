from django.conf.urls import include, url
from django.contrib import admin
from wddoersite.wddoer.views import LoginView


urlpatterns = [
    # Examples:
    # url(r'^$', 'wddoersite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('wddoersite.blog.urls')),

    url(r'^blog_admin/', include('wddoersite.blog_admin.urls')),
    url(r'^login/', LoginView.as_view(), name='login_view'),

]
