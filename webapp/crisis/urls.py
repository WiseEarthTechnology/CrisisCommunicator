from django.conf.urls.defaults import *

from views import home

urlpatterns = patterns('',
        (r'^/$', home),
)
