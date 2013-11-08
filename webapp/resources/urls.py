from django.conf.urls.defaults import *

from views import resource, delete_resource

urlpatterns = patterns('',
        (r'^/$', resource),
        (r'^/add/$',resource),
        (R'^/delete/$', delete_resource),
)
