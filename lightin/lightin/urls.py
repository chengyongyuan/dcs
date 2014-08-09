from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mobiconf.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mobi/',  include('mobiconf.urls', namespace='mobiconf')),
    url(r'^datapanel/', include('datapanel.urls', namespace='datapanel')),
    url(r'^admin/', include(admin.site.urls)),
)
