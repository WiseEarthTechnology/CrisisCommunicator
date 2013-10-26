"""
Redistribution and use of the software accompanying this license in source and 
binary forms, with or without modification, are permitted provided that the 
following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, 
	this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright 
	notice, this list of conditions and the following disclaimer in the 
	documentation and/or other materials provided with the distribution.
    3. Modifications to the source code must retain the above copyright 
	notice, this list of conditions, and the following disclaimer, and may 
	not include further conditions or licensing which go against the spirit 
	of this license.
    4. This software may not be used to cause deliberate harm to any 
	individual, either directly or indirectly, in any form.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER, AUTHORS, OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE 
GOODS OR SERVICES; LOSS OF USE, DATA, MONEY, POSSESSIONS, OR LIFE; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
OF SUCH DAMAGE.
"""
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
