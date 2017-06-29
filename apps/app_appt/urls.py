from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^dashboard$', views.dashboard , name ='dashboard'),
    url(r'^addappointment$', views.addappointment , name ='addappointment') ,
    url(r'^editappt/(?P<id>\d+)$$', views.editappt , name ='editappt') ,
     url(r'^deleteappt/(?P<id>\d+)$$', views.deleteappt , name ='deleteappt') ,
    url(r'^logout$', views.logout , name ='logout')  
 
    ]