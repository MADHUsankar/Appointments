from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..app_reglogin.models import User
from .models import Appointment
from django.core.urlresolvers import reverse
from datetime import date
from datetime import datetime
import time 
import bcrypt

# Create your views here.
def dashboard(request):
    #Tripschedule.objects.all().delete()
    #datetime.strptime(postData['startdate'], '%Y-%m-%d').date()
    today = datetime.now()
    print "today date"
    print today
    context = { 
                    'otherappts' :  Appointment.objects.all().exclude(apptdate=today),
                    'todayappt' :  Appointment.objects.filter(apptdate=today),
                    "name": request.session['name'],             
                    "userid" :  request.session['userid'] ,
                    "date" : datetime.today() 
                }
   
    return render(request,'app_appt/dashboard.html', context)


def addappointment(request):

    if request.method == "POST":
        print request.POST
        context = {
                "name": request.session['name'],
                "userid" :  request.session['userid'] 
                }
      
        result = Appointment.objects.addappointment(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "not added"
            return redirect(reverse('appointments:dashboard'))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('appointments:dashboard'))
            
    else:
            print "ENTERED GET"
            context = {
                    'appointment' :  Appointment.objects.all(),
                    "name": request.session['name']    
             }
    return render(request,'app_appt/dashboard.html',context )



def logout(request):
    request.session.clear()
    return redirect('users:my_index')


def editappt(request,id):
    if request.method == "POST":
        context = {
                "name": request.session['name'],
                "userid" :request.session['userid'],
                "apptid" : id
                }
        
        result = Appointment.objects.editappt(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
                return redirect(reverse('appointments:editappt',kwargs={'id': id}))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('appointments:dashboard'))
    else:
        context = {
            'appt' :Appointment.objects.get(id=id)

            }
            #return redirect(reverse('show',kwargs={'id':id}))
    return render(request,'app_appt/editappt.html', context)

def deleteappt(request,id):
    Appointment.objects.filter(id=id).delete()
    return redirect(reverse('appointments:dashboard'))



