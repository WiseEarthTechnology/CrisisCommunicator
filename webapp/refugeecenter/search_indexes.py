"""
Filename: refugeecenter/search_indexes.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
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





