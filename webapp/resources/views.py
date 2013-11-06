from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from random import randint

from forms import ResourceForm
from crisis.forms import CommentForm
from crisis.models import Comment, User, Global
from crisis.helper import generate_gid
from models import Supply, Resource
from helper import update_supply

def resource(request):

    """
    View to enter resource details into the crisis communicator. This help the response personal \
    to find out the location or direct the refugees as per the updates. 

    """

    if request.method == 'POST':
        resource_form = ResourceForm(request.POST)
        comment_form = CommentForm(request.POST)
        valid_resource_form = resource_form.is_valid()
        valid_comment_form = comment_form.is_valid()

        if valid_resource_form and valid_comment_form:
            if request.POST['quantity'] != '' and request.POST['req_quantity'] != '':
                quantity = int(request.POST['quantity'])
                req_quantity = int(request.POST['req_quantity'])
            else:
                quantity = 0
                req_quantity = 0
            
            comment_form_data = comment_form.save(commit=False)
            _comment_id = randint(1,10000)
            comment_form_data.comment_id = _comment_id
            comment_form_data.user_id = get_object_or_404(User, user_id=request.session['user_id'])
            comment_form_data.save()
            resource_form_data = resource_form.save(commit=False)
            
            supply_obj = get_object_or_404(Supply, pk=update_supply(quantity, str(request.POST['measurement'])))
            required_supply_obj = get_object_or_404(Supply, pk=update_supply(req_quantity, str(request.POST['req_measurement'])))
            resource_form_data.supply = supply_obj
            resource_form_data.supply_requirement = required_supply_obj
            resource_form_data.gid = generate_gid()
            resource_form_data.comment = get_object_or_404(Comment, comment_id=_comment_id)
            resource_form_data.save()
            return HttpResponseRedirect('/crisis/')
        else:
            return render_to_response('resource/resource.html', {'comment_form':comment_form,\
                    'resource_form':resource_form}, RequestContext(request))

    else:
        initial = {}
        if request.GET.get('q') is not None:
            lnglat = request.GET.get('q').split(",")
            initial = {
                'latitude':float(lnglat[0]),
                'longitude':float(lnglat[1]),
            }

        return render_to_response('resource/resource.html', {'comment_form':CommentForm(),\
                                    'resource_form':ResourceForm(initial)}, RequestContext(request))


def delete_resource(request):
    
    if request.method == 'GET':
        try:
            resource_id = Resource.objects.get(pk=str(request.GET['q']))
            resource_id.delete()
            return HttpResponseRedirect('/crisis/')
        except:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/crisis/')


