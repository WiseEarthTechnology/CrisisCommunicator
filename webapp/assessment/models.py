"""

__author__ = "Seshagiri Prabhu"
__copyright__ = "Copyright 2013, Wise Earth Technology"
__credits__ = ["Bithin Alangot"]
__license__ = "PeaceOSL"

"""
from django.db import models

from crisis.models import Global, Comment

class RoadAssessment(models.Model):
    """
    Store the details of the roads in the disaster area.

    """
    gid = models.ForeignKey(Global)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    assessment = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, blank=True, null=True)

    class Meta:
        db_table = 'crisis_roadAssessment'

    def __unicode__(self):
        return self.assessment


class Rendezvous(models.Model):
    """
    Details regarding each meeting. 
    
    location: The place where the meeting should be organized.

    date: Data and Time of the meeting.

    """
    gid = models.ForeignKey(Global)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'crisis_rendezvous'

    def __unicode__(self):
        return self.location


class Emergency(models.Model):
    """
    Details regarding the emergency is stored in this table.

    severity: It is rated from 1 to 5.

    Service_required: Medical, Food etc

    Cause: What led to the emergence situation.

    """
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    gid = models.ForeignKey(Global)
    severity = models.IntegerField(null=True, blank=True)
    service_required = models.CharField(max_length=200, null=True, blank=True)
    cause = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, blank=True, null=True)

    class Meta:
        db_table = 'crisis_emergency'

    def __unicode__(self):
        return self.cause


class Crime(models.Model):
    """
    Details of the crime that may happen in a diseater zone
    
    Criminal: No. of Criminal in specified location. 

    crime_type: kidnapping, rape, killing etc

    """
    gid = models.ForeignKey(Global)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    crime_type = models.CharField(max_length=100, blank=True, null=True)
    criminals = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, blank=True, null=True)

    class Meta:
        db_table = 'crisis_crime'

    def __unicode__(self):
        return self.crime_type
    
