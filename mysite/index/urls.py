# accounts/urls.py
from django.conf.urls import url
from index import views
# SET THE NAMESPACE!
app_name = 'index'
from django.views.decorators.csrf import csrf_exempt

# Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    url(r'^$',views.main,name='index'),
    url('flights', views.flights),
    url('addnewflight', views.addNewFlight),
    url('tickets', views.tickets),
    url('addnewticket', views.addNewTicket),
    url('agency', views.agency),
    url('addnewagency', views.addNewAgency),
    url('airports', views.airport),
    url('addnewairport', views.addNewAirport),
    url('addnewcrew', views.addNewCrew),
    url('crew', views.crew),
    url('addnewaircraft', views.addNewAircraft),
    url('aircraft', views.aircraft),


]