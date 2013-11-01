"""

__author__ = "Seshagiri Prabhu"
__copyright__ = "Copyright 2013, Wise Earth Technology"
__credits__ = ["Bithin Alangot"]
__license__ = "PeaceOSL"

"""

from django.forms import ModelForm
from django import forms

from models import Rendezvous, Emergency, Crime, RoadAssessment

class RendezvousForm(ModelForm):
    """
    Return a empty form to create a meeting. 
    
    rtype: HTML Form

    """

    class Meta:
        model = Rendezvous
        exclude = ('gid')


class EmergencyForm(ModelForm):
    """
    Return a empty form to report emergency.

    rtype: HTML Form 

    """

    class Meta:
        model = Emergency 
        exclude = ('gid', 'comment')
        widgets = {
            'latitude': forms.TextInput(attrs={'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder':'Longitude'}),
            'severity': forms.TextInput(attrs={'placeholder':'Severity of the emergency'}),
            'service_required': forms.TextInput(attrs={'placeholder':'Service required if any'}),
            'cause': forms.TextInput(attrs={'placeholder':'Cause of the emergency'}),
        }

class CrimeForm(ModelForm): 
    """
    Return a empty form to report crime in a area.

    rtype: HTML Form

    """

    class Meta:
        model = Crime
        exclude = ('gid','comment')
        widgets = {
            'latitude': forms.TextInput(attrs={'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder':'Longitude'}),
            'crime_type': forms.TextInput(attrs={'placeholder':'Crime Type'}),
            'criminals': forms.TextInput(attrs={'placeholder':'Number of Criminals'}),
        }

class CrimeUpdateForm(ModelForm):
    class Meta:
        model = Crime
        exclude = ('gid', 'date', 'comment')

class RoadAssessmentForm(ModelForm):
    """
    Return a empty form to make road assessment

    rtype: HTML Form 

    """

    class Meta:
        model = RoadAssessment
        exclude = ('gid', 'comment')
        widgets = {
            'latitude': forms.TextInput(attrs={'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder':'Longitude'}),
            'assessment': forms.TextInput(attrs={'placeholder':'Assessment Level'}),
        }

