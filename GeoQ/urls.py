from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import maps.views

# Examples:
# url(r'^$', 'pyTravelogue.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', maps.views.index, name='index'),
    url(r'^db', maps.views.db, name='db'),
    #url(r'^login', maps.views.login, name='login'),
    #url(r'^signup', maps.views.signup, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
]
