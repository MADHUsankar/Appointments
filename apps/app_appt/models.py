# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_reglogin.models import User
from django.db import models
from datetime import date
from datetime import datetime
import time 
import bcrypt

 
class appointmentManager(models.Manager):
    def addappointment(request,postData,sessiondata):
        print postData
        print " In addappointment %%%%%%%%%%%"
        
        results = {'status': True, 'errors': []}
        if not postData['tasks'] or len(postData['tasks'])<1:
            print "In tasks "
            results['status'] = False
            results['errors'].append("Please enter a task")

 
        if not postData['apptdate'] or len(postData['apptdate'])<1:
            print "In startdate "
            results['status'] = False
            results['errors'].append("Please enter an Appointment date")
        if not postData['appttime'] or len(postData['appttime'])<1:
            print "In returndate "
            results['status'] = False
            results['errors'].append("Please enter appointment time")

        if results['status']:   
            today = datetime.now().date()
            appdate = datetime.strptime(postData['apptdate'], '%Y-%m-%d').date()
            
       
            if appdate < today :  
                results['status'] = False
                results['errors'].append('Appointment Date must be in the future.')

            apptime = datetime.strptime(postData['appttime'], '%H:%S').time()
            currenttime = datetime.now().time()
            if  appdate == today and apptime < currenttime:  
                results['status'] = False
                results['errors'].append('Appointment Time   must be in the future.')




        if results['status']:
            user1 = User.objects.get(id = sessiondata['userid'])
            appointment1 = Appointment.objects.create(Tasks=postData['tasks'],
            apptdate=postData['apptdate'],appttime=postData['appttime'],apptuser = user1)
        
          
            results['status'] = True
            print "Added"
            #print apptdate.apptdate
       
        return results            

    def editappt(request,postData,sessiondata):
        print postData
        print " In editappt %%%%%%%%%%%"
        
        results = {'status': True, 'errors': []}
        if not postData['tasks'] or len(postData['tasks'])<1:
            print "In tasks "
            results['status'] = False
            results['errors'].append("Please enter a task")

 
        if not postData['apptdate'] or len(postData['apptdate'])<1:
            print "In startdate "
            results['status'] = False
            results['errors'].append("Please enter an Appointment date")



        if not postData['appttime'] or len(postData['appttime'])<1:
            print "In returndate "
            results['status'] = False
            results['errors'].append("Please enter appointment time")



        if results['status']:   
            today = datetime.now().date()
            appdate = datetime.strptime(postData['apptdate'], '%Y-%m-%d').date()
            
       
            if appdate < today :  
                results['status'] = False
                results['errors'].append('Appointment Date must be in the future.')

            apptime = datetime.strptime(postData['appttime'], '%H:%S').time()
            currenttime = datetime.now().time()
            if  appdate == today and apptime < currenttime:  
                results['status'] = False
                results['errors'].append('Appointment Time   must be in the future.')
 
        
        if results['status']:
            user1 = User.objects.get(id = sessiondata['userid'])
            appointment1 = Appointment.objects.get(id=sessiondata['apptid'])
            appointment1.apptdate = postData['apptdate'] 
            appointment1.appttime=postData['appttime']
            appointment1.Tasks=postData['tasks'] 
            appointment1.apptstatus=postData['apptstatus'] 
            appointment1.save()
             
        return results            






class Appointment(models.Model):
    Tasks = models.TextField(max_length=1000)
    apptdate =  models.DateField({'input_formats': ('%Y-%m-%d',)})
    appttime = models.TimeField()
    apptstatus = models.CharField(max_length=38,default = 'pending')
    apptuser= models.ForeignKey('app_reglogin.User', related_name="apptuser")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     
    objects=appointmentManager()
    #bookauthors