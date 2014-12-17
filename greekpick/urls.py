from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'greekpick.views.index', name='index'),
    url(r'^vote/(.*)$', 'greekpick.views.vote', name='vote'),
)
