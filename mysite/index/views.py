from django.shortcuts import render

# Create your views here.
from django.forms.models import model_to_dict

from django.http import HttpResponse

from django.template import loader
from index.forms import FlightForm
from index.models import Flight, Ticket, Agency
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def main(request):
    template = loader.get_template('index/myindex.html')
    context = {
        'data': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))

def flights(request):
    template = loader.get_template('index/airportFlights.html')
    context = {
        'data': 'latest_question_list',
    }    

    return HttpResponse(template.render(context, request))


@csrf_exempt 
def addNewFlight(request):
    # modle Add newTicket ham mitoonam beznam
    template_name  = 'index/addNewFlight.html'
    template = loader.get_template('index/addNewFlight.html')

    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            f = Flight(flight_no=data['flight_no'],
             s_city=data['s_city'], d_city=data['d_city'], time_1=data['time_1'], time_2= data['time_2'], capacity=data['capacity'])
            f.save()
            form = FlightForm()

        arg = {"form":form, 'data': data}
        return render(request, template_name, arg)

    else:
        form = FlightForm()
        return render(request, template_name, {"form":form})

    #     return HttpResponse(template.render({"form":form}, request))

    
def tickets(request):
    template = loader.get_template('index/airportTickets.html')

    ticket_list = [t.flight_no for t in Ticket.objects.all()]
    flights_data = []
    for item in ticket_list:
        obj = Flight.objects.get(flight_no=item)
        serialized_obj = model_to_dict(obj)
        flights_data.append(serialized_obj)
    
    context = {'data': flights_data}
    print(context)

    return HttpResponse(template.render(context, request))


@csrf_exempt 
def addNewTicket(request):
    template = loader.get_template('index/addNewTicket.html')

    if request.method == 'POST':
        flight_no = request.POST.get('flight_no')
        # print(request.POST.get('flight_no'))
        t = Ticket(flight_no=int(flight_no))
        t.save()
    return render(request, 'index/addNewTicket.html', {"data": flight_no})


    
def agency(request):
    template = loader.get_template('index/airportAgencies.html')
    context = {'data': []}
    obj = Agency.objects.all()
    
    agency_data = []
    for item in obj:
        serialized_obj = model_to_dict(item)
        agency_data.append(serialized_objb)

    context = {'data': agency_data}
    print(context)
    return HttpResponse(template.render(context, request))
