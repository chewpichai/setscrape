from django.conf.urls import patterns, include, url
from django.contrib import admin
from setscrape import settings, views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.get_index, name='setscrape.index'),
    url(r'^api/$', views.get_api, name='setscrape.api'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<symbol>[-+&\w%]+)/$', views.get_symbol, name='setscrape.symbol'),
)
