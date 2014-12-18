from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'poll.views.index', name='index'),
    url(r'^results$', 'poll.views.results', name='results'),
    url(r'^vote/(.*)$', 'poll.views.vote', name='vote'),
)
