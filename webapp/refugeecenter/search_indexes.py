import datetime
from haystack import indexes
from models import RefugeeCenter


class RefugeeCenterIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(use_template=True, document=True)
    place = indexes.CharField(model_attr='place')
    center_id = indexes.CharField(model_attr='center_id')


    def get_model(self):
        return RefugeeCenter

    def get_queryset(self):
        "Used when the entire index for model is updated."
        return RefugeeCenter.objects.all()





