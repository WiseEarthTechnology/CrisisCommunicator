import datetime
from haystack import indexes
from models import Person, Refugee, Deceased, Missing


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(use_template=True, document=True)
    person_name = indexes.CharField(model_attr='person_name')
    person_id = indexes.CharField(model_attr='person_id')
    gender = indexes.CharField(model_attr='gender')


    def get_model(self):
        return Person

    def get_queryset(self):
        "Used when the entire index for model is updated."
        return Person.objects.all()



"""
class RefugeeIndex(indexes.SearchIndex):
    person_id = indexes.CharField(use_template=True, model_attr='person_id')
    center_id = indexes.CharField(model_attr='center_id')

    def get_model(self):
        return Refugee
    
    def get_queryset(self):
        return Person.objects.all().filter(person_id=person_id)


class DeceasedIndex(indexes.SearchIndex):
    person_id = indexes.CharField(use_template=True, model_attr='person_id')
    idenified = indexes.CharField(model_attr='identified')
    date = indexes.CharField(model_attr='date')
    latitude = indexes.CharField(model_attr='latitude')
    longitude = indexes.CharField(model_attr='longitude')
    
    def get_model(self):
        return Deceased
    
    def get_queryset(self):
        return Person.objects.all().filter(person_id=person_id)


class MissingIndex(indexes.SearchIndex):
    person_id = indexes.CharField(use_template=True, model_attr='person_id')
    missing_id = indexes.CharField(model_attr='missing_id')

    def get_model(self):
        return Missing

    def get_queryset(self):
"""

