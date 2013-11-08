from django.conf.urls.defaults import *
from views import refugee_center, refugee_center_update, refugee_center_list, \
                    search_refugeecenter, autocomplete, delete_refugeecenter

urlpatterns = patterns('',
        (r'^/$', refugee_center_list),
        (r'^/search/', search_refugeecenter),
        (r'^/autocomplete/$', autocomplete),
        (r'^/add/$', refugee_center),
        (r'^/delete/$', delete_refugeecenter),
        (r'^/(?P<center_id>\w+)/update/$',refugee_center_update), 
)


