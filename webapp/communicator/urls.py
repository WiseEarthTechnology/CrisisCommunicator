from django.conf.urls.defaults import *
from communicator.views import user_home, user_register, logout

urlpatterns = patterns('',
    (r'^$', user_home),
    (r'^crisis', include('crisis.urls')),
    (r'^assessment', include('assessment.urls')), 
    (r'^person', include('person.urls')),
    (r'^refugeecenter', include('refugeecenter.urls')),
    (r'^resource', include('resources.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^register/$', user_register),
    (r'^logout/$', logout),
)
