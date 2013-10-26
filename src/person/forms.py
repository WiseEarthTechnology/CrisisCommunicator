from django.forms import ModelForm
from django import forms

from models import Person, Refugee, Missing, Deceased
from refugeecenter.models import RefugeeCenter

class PersonForm(ModelForm):
    """
    Returns a empty form to enter the details of a Person.

    :rtype: HTML Form

    """

    class Meta:
        model = Person
        widgets = {
               'person_id': forms.TextInput(attrs={'placeholder':'Person ID', 'label': ''}),
               'person_name': forms.TextInput(attrs={'placeholder':'Person Name'}),
               'gender': forms.RadioSelect(),
               'age': forms.TextInput(attrs={'placeholder':'Age'}),
               'hair_color': forms.TextInput(attrs={'placeholder':'Hair Colour'}),
               'height': forms.TextInput(attrs={'placeholder':'Height'}),
               'wounds': forms.RadioSelect(),
               'identification_mark': forms.TextInput(attrs={'placeholder':'Identification Mark'}),
               'color_complexation': forms.TextInput(attrs={'placeholder':'Colour Complexion'}),
        }

class PersonUpdateForm(ModelForm):
    class Meta:
        model = Person
        exclude =('person_id')


class RefugeeForm(ModelForm):
    """
    Returns a empty form to enter the details of a Refugee. 

    :rtype: HTML Form

    """

    class Meta:
        model = Refugee
        exclude = ('person_id', 'gid')
        widgets = {
                'center_id': forms.Select(),
                'health_status': forms.TextInput(attrs={'placeholder':'Health Status'}),
        }

    def __init__(self, *args, **kwargs):
        super(RefugeeForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['center_id'].queryset = RefugeeCenter.objects.all()
            self.fields['center_id'].empty_label = "Select a Refugee Center"
            self.fields['center_id'].widget.choices = self.fields['center_id'].choices

class RefugeeUpdateForm(ModelForm):
    class Meta:
        model = Refugee
        exclude = ('person_id', 'gid')

class MissingForm(ModelForm):
    """
    Returns a empty form to enter the details of a Missing person. 

    :rtype: HTML Form 

    """

    class Meta:
        model = Missing
        exclude = ('person_id', 'gid', 'comment', 'last_seen')
        widgets = {
               'missing_id': forms.TextInput(attrs={'placeholder':'Missing Person\'s ID'}),
        }


class DeceasedForm(ModelForm):
    """
    Returns a empty form to enter the details of a deceased person.

    :rtype: HTML Form

    """

    class Meta:
        model = Deceased
        exclude = ('person_id', 'gid')
        widgets = {
            'latitude': forms.TextInput(attrs={'placeholder':'Latitude'}),
            'longitude': forms.TextInput(attrs={'placeholder':'Longitude'}),
            'identified': forms.RadioSelect(),
        }

class DeceasedUpdateForm(ModelForm):
    class Meta:
        model = Deceased
        exclude = ('person_id', 'gid')
