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
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import get_template
from django.core.context_processors import csrf

from forms import UserEnterForm, UserRegisterForm
from crisis.models import User, TrackCommunicator


"""
View to display the home page. User has to type in the user id or his name to 
enter the device. This is just to make sure who is using which device and 
take care of the response personal.

"""
def user_home(request):
    
    device = TrackCommunicator(internal_id='amrita', longitude='34.19', latitude='45.34')
    device.save()
    if request.method == 'POST':
        _user_id = str(request.POST['user_id'])
        name = str(request.POST['name'])
        user_tuple_id = User.objects.all().filter(user_id=_user_id)
        if user_tuple_id:             
            user_update = User.objects.get(user_id=_user_id)
            user_update.internal_id = get_object_or_404(TrackCommunicator, internal_id='amrita')
            request.session['loggedInside'] = True
            request.session['user_id'] = _user_id
            return HttpResponseRedirect("/crisis/")
        else:
            return HttpResponseRedirect("/register/?user_id="+_user_id+"&name="+name+"")
    else:
        return render_to_response('general/home.html',{'user_form':UserEnterForm()},RequestContext(request))	


"""
View to display the register template.

"""
def user_register(request):

    device = TrackCommunicator(internal_id='amrita', longitude='34.19', latitude='45.34')
    device.save()
    if request.method == 'POST':
        user_register_form = UserRegisterForm(request.POST)
        valid_user_form = user_register_form.is_valid()
        if valid_user_form:
            form_data = user_register_form.save(commit=False)
            form_data.internal_id = get_object_or_404(TrackCommunicator, internal_id='amrita')
            cleaned_user_form_data = user_register_form.cleaned_data
            cleaned_userid = cleaned_user_form_data['user_id']
            request.session['loggedInside'] = True
            request.session['user_id'] = cleaned_userid
            user_register_form.save()
            return HttpResponseRedirect("/crisis/")
        else:
            return render_to_response('general/register.html',{'register_form':UserRegisterForm(), 'error':'You have an error'}, RequestContext(request))

    else:
        initial = {
            'user_id':str(request.GET['user_id']),
            'name':str(request.GET['name']),
        }
        return render_to_response('general/register.html',{'register_form':UserRegisterForm(initial)},RequestContext(request))


"""
Simple logout page.

"""
def logout(request):
    try:
        del request.session['loggedinside']
        request.session.flush()
    except KeyError:
        pass
    return HttpResponseRedirect("/")
