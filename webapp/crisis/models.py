"""
Filename: crisis/models.py
Authors: Bithin Alangot Seshagiri Prabhu Harish Navnit
Copyright: Wise Earth Technology
This file is part of the CrisisCommunicator Project.  
It is licensed under the Peaceful Open Source License.  
Please see the license terms in PeaceOSL.txt
"""
from django.db import models
#from refugeecenter.models import RefugeeCenter

ROLES = (
    ('Chief','Chief'),
    ('Volunteer', 'Volunteer'),
    ('Army', 'Army'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)



YES_NO = ((True, 'Yes'), (False, 'No'))

IDENTIFIED = (('Y', 'Person Identified'), ('N', 'Person not yet identified'))

class TrackCommunicator(models.Model):
    """
    Keep track of the location of the crisis communicator. 
    This will have the list of crisis communicator and their
    corresponding locations.

    Internal ID : An ID specific to the device.
    
    """

    internal_id = models.CharField(max_length=100, primary_key=True)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, 
                    decimal_places=10)

    
    class Meta: 
        db_table = 'crisis_track'

    def __unicode__(self):
        return self.internal_id


class Global(models.Model):
    """
    This table logs all the message that are generated in this device. 

    GID : Disaster Wide Identifier ( Internal ID + TimeStamp ) 
    Internal ID : The ID of the device 
    CSV Update : List of Update GID's 
    Response Status : Whether all the crisis communicator has updated 
                        the change. 

    """

    gid = models.CharField(max_length=200, primary_key=True)
    internal_id = models.ForeignKey(TrackCommunicator) 
    csv_update = models.CharField(max_length=300) 
    response_status = models.BooleanField()


    class Meta: 
        db_table = 'crisis_global'

    def __unicode__(self):
        return self.gid

class User(models.Model):
    """
    The details of the rescue works who use the crisis communicator
    
    Role: Response Personal Role in Disaster Zone.

    Internal ID: Used to identify which device the user is using. 

    """

    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    internal_id = models.ForeignKey(TrackCommunicator, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=10, default='M')
    health_status = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(choices=ROLES, max_length=10, default='Volunteer')
    
    class Meta:
        db_table = 'crisis_user'

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    """
    It stores the comment from all the tables

    """
    comment_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User)
    comment = models.CharField(max_length='300', blank=True)

    class Meta:
        db_table = 'crisis_comment'

    def __unicode__(self):
        return self.comment
