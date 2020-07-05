# accounts/urls.py
from django.conf.urls import url
from index import views
# SET THE NAMESPACE!
app_name = 'index'
# Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    url(r'^$',views.main,name='index'),
    url('flights', views.flights),
    url('addnewflight', views.addNewFlight),
    url('tickets', views.tickets),
    url('addnewticket', views.addNewTicket),
    url('agency', views.agency),


]