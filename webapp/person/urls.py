from django.conf.urls.defaults import *

from views import refugee, missing, deceased, refugee_list, missing_list, \
                    refugee_autocomplete, deceased_autocomplete, \
                    deceased_list, autocomplete, search_refugee, refugee_update, deceased_update


urlpatterns = patterns('',
        (r'^/$', refugee),
        (r'^/search/', search_refugee),
        (r'^/autocomplete/$', autocomplete),

        (r'^/refugee/add/$', refugee), 
        (r'^/refugee/list/$', refugee_list),
        (r'^/refugee/autocomplete/$', refugee_autocomplete), 
        (r'^/refugee/(?P<person_id>\w+)/update/$',refugee_update),
        
        (r'^/missing/add/$', missing),
        (r'^/missing/list/$', missing_list),

        (r'^/deceased/add/$', deceased),
        (r'^/deceased/autocomplete/$', deceased_autocomplete),
        (r'^/deceased/list/$', deceased_list),
        (r'^/deceased/(?P<person_id>\w+)/update/$',deceased_update),
        
)
