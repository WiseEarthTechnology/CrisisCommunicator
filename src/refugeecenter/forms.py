from django.forms import ModelForm
from django import forms

from models import RefugeeCenter

class RefugeeCenterForm(ModelForm):
    """
    Returns a empty form to enter the details of a Refugee 
    Center.

    :rtype: HTML Form

    """

    class Meta:
        model = RefugeeCenter
        exclude = ('gid')
        widgets = {
            'center_id':forms.TextInput(attrs={'placeholder':'Center ID'}),
            'place': forms.TextInput(attrs={'placeholder':'Location Name'}),
            'latitude': forms.TextInput(attrs={'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder':'Longitude'}),
            'population': forms.TextInput(attrs={'placeholder':'Population'}),
            'population_capacity': forms.TextInput(attrs={'placeholder':'Total Capacity'}),
            'supplies_available_for': forms.TextInput(attrs={'placeholder':'Supplies Available For'}),
        }

class RefugeeCenterUpdateForm(ModelForm):

    class Meta:
        model = RefugeeCenter
        exclude = ('gid', 'center_id')
