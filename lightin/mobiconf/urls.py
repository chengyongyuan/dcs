from django.conf.urls import patterns, include, url
from mobiconf.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',  index, name='index'),
    url(r'getmargin', getmargin, name = 'getmargin'),
)
