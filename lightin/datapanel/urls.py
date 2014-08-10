from django.conf.urls import patterns, include, url
from datapanel.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',  index, name='index'),
    url(r'login$', login, name='login'),
)
