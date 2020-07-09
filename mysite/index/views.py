from django.shortcuts import render

# Create your views here.
from django.forms.models import model_to_dict

from django.http import HttpResponse

from django.template import loader
from index.forms import FlightForm
from index.models import Flight, Ticket, Agency, Airport, Crew, Aircraft
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def main(request):
    template = loader.get_template('index/myindex.html')
    context = {
        'data': [],
    }
    return HttpResponse(template.render(context, request))

def flights(request):
    template = loader.get_template('index/airportFlights.html')
    context = {'data': []} 

    f = Flight.objects.all()
    crew_list = []
    counter = 0
    airplane_list = {new_list: [] for new_list in range(len(f))} 
    crew_list = {new_list: [] for new_list in range(len(f))}
    passenger_list = {new_list: [] for new_list in range(len(f))}

    for item in f:
        json = model_to_dict(item)
        context['data'].append(json)

        for data in json['crew'] :
            crew_list[counter].append(model_to_dict(data))
        
        for data1 in json['airplane']:
            # print(model_to_dict(data1))
            airplane_list[counter].append(model_to_dict(data1))

        for data2 in json['passenger']:
            passenger_list[counter].append(model_to_dict(data2))
        counter += 1
    print(airplane_list)
    inner_list = []
    inner_list_1 = []
    for i in range(len(context['data'])):
        print(i)
        context['data'][i]['crew'] = crew_list[i]
        context['data'][i]['airplane'] = airplane_list[i]
        context['data'][i]['passenger'] = passenger_list[i]
        # if context['data'][i]['airport'] is not None:
        context['data'][i]['airport'] = [model_to_dict(Airport.objects.get(id = int(context['data'][i]['airport'] )))]
        for data4 in context['data'][i]['airport']:
            # print(data4['airplane'])
            for obj in data4['airplane']:
                inner_list.append(model_to_dict(obj))
            for obj1 in data4['agency']:
                inner_list_1.append(model_to_dict(obj1))
            
        context['data'][i]['airport'][0]['airplane'] = inner_list
        context['data'][i]['airport'][0]['agency'] = inner_list_1
    print('\n')
    print(context)
    print("**************\n")

    return HttpResponse(template.render(context, request))


@csrf_exempt 
def addNewFlight(request):
    # modle Add newTicket ham mitoonam beznam
    template_name  = 'index/addNewFlight.html'
    template = loader.get_template('index/addNewFlight.html')
    if request.method=='POST':
        flight_no = request.POST.get('flight_no')
        s_city = request.POST.get('s_city')
        d_city = request.POST.get('d_city')
        time_1 = request.POST.get('time_1')
        time_2 = request.POST.get('time_2')
        capacity = request.POST.get('capacity')
        pilot = request.POST.get('pilot')
        crew = request.POST.get('crew')
        airplane = request.POST.get('airplane')
        passenger = request.POST.get('passenger')
        airport = request.POST.get('airport')

        f = Flight(flight_no=flight_no,
         s_city=s_city, d_city=d_city, time_1=time_1, time_2= time_2, capacity=capacity
         , pilot=pilot, crew =crew, airplane = airplane, passenger=passenger, airport=airport)
        f.save()    # if request.method == 'POST':
        
    return render(request, template_name, {})

        # return HttpResponse(template.render({"form":form}, request))

    #     form = FlightForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         data = form.cleaned_data
    #         f = Flight(flight_no=data['flight_no'],
    #          s_city=data['s_city'], d_city=data['d_city'], time_1=data['time_1'], time_2= data['time_2'], capacity=data['capacity']
    #          , pilot=data['pilot'], crew =data['crew'], airplane = data['airplane'], passenger=data['passenger'], airport=data['airport'])
    #         f.save()
    #         form = FlightForm()

    #     arg = {"form":form, 'data': data}
    #     return render(request, template_name, arg)

    # else:
    #     form = FlightForm()
    #     return render(request, template_name, {"form":form})

    #     return HttpResponse(template.render({"form":form}, request))

    
def tickets(request):
    template = loader.get_template('index/airportTickets.html')
    context = {'data': []} 
    ticket_list = [t.flight_no for t in Ticket.objects.all()]
    flights_list_obj = []
    for item in ticket_list:
        obj = Flight.objects.get(flight_no=item)
        flights_list_obj.append(obj)
    print(flights_list_obj)
    f = flights_list_obj
    crew_list = []
    counter = 0
    airplane_list = {new_list: [] for new_list in range(len(f))} 
    crew_list = {new_list: [] for new_list in range(len(f))}
    passenger_list = {new_list: [] for new_list in range(len(f))}

    for item in f:
        json = model_to_dict(item)
        context['data'].append(json)

        for data in json['crew'] :
            crew_list[counter].append(model_to_dict(data))
        
        for data1 in json['airplane']:
            # print(model_to_dict(data1))
            airplane_list[counter].append(model_to_dict(data1))

        for data2 in json['passenger']:
            passenger_list[counter].append(model_to_dict(data2))
        counter += 1
    # print(airplane_list)
    inner_list = []
    inner_list_1 = []
    for i in range(len(context['data'])):
        # print(i)
        context['data'][i]['crew'] = crew_list[i]
        context['data'][i]['airplane'] = airplane_list[i]
        context['data'][i]['passenger'] = passenger_list[i]
        # if context['data'][i]['airport'] is not None:
        context['data'][i]['airport'] = [model_to_dict(Airport.objects.get(id = int(context['data'][i]['airport'] )))]
        for data4 in context['data'][i]['airport']:
            # print(data4['airplane'])
            for obj in data4['airplane']:
                inner_list.append(model_to_dict(obj))
            for obj1 in data4['agency']:
                inner_list_1.append(model_to_dict(obj1))
            
        context['data'][i]['airport'][0]['airplane'] = inner_list
        context['data'][i]['airport'][0]['agency'] = inner_list_1
    print(context)

    return HttpResponse(template.render(context, request))

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

@csrf_exempt 
def addNewTicket(request):
    template = loader.get_template('index/addNewTicket.html')

    if request.method == 'POST':

        try:
            flight_no = request.POST.get('flight_no')
        except IntegrityError as e: 
            print(e)
            print("*************")
            if 'unique constraint' in e.message:
                print("HERE")

        t = Ticket(flight_no=int(flight_no))
        t.save()
    print("CREATED")
    return render(request, 'index/addNewTicket.html', {"data": flight_no})


    
def agency(request):
    template = loader.get_template('index/airportAgencies.html')
    context = {'data': []}
    obj = Agency.objects.all()
    
    agency_data = []
    for item in obj:
        serialized_obj = model_to_dict(item)
        agency_data.append(serialized_obj)

    context = {'data': agency_data}
    print(context)
    return HttpResponse(template.render(context, request))


@csrf_exempt 
def addNewAgency(request):
    template = loader.get_template('index/addNewAgency.html')
    template_name = 'index/addNewAgency.html'

    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        contract_s_date = request.POST.get('contract_s_date')
        contract_d_ate = request.POST.get('contract_d_ate')
        contract_number = request.POST.get('contract_number')
        a = Agency(name=name, city=city, contract_s_date=contract_s_date, contract_d_ate=contract_d_ate, contract_number=contract_number)    
        a.save()
    print("CREATED")
    return render(request, template_name, {})


def airport(request):
    template = loader.get_template('index/airports.html')
    context = {'data': []}
    obj = Airport.objects.all()
    # f = flights_list_obj
    f = obj

    counter = 0
    airplane_list = {new_list: [] for new_list in range(len(f))} 
    agency_list = {new_list: [] for new_list in range(len(f))}

    for item in f:
        json = model_to_dict(item)
        context['data'].append(json)

        for data in json['agency'] :
            agency_list[counter].append(model_to_dict(data))
        
        for data1 in json['airplane']:
            # print(model_to_dict(data1))
            airplane_list[counter].append(model_to_dict(data1))

        counter += 1
    # print(airplane_list)
    inner_list = []
    inner_list_1 = []
    for i in range(len(context['data'])):
        # print(i)
        context['data'][i]['agency'] = agency_list[i]
        context['data'][i]['airplane'] = airplane_list[i]
    print(context)

    return HttpResponse(template.render(context, request))

# name migiram
def airportMoreInfo(request):
    template_name  = 'index/airportsMoreInfo.html'
    template = loader.get_template('index/airportsMoreInfo.html')
    # airplane_list = {new_list: [] for new_list in range(len(f))} 

    context= {'flight':[],'ticket':[], 'crew':[], 'airplane':[], 'agency':[]}
    if request.method == 'POST':
        name = request.POST.get('name')
        airport = Airport.objects.get(name=name)
        # print(airport)
        f = Flight.objects.filter(airport=airport)
        t = []
        c = []
        for data in f:
            # print(Ticket.objects.filter(flight_no = model_to_dict(data)['flight_no']))
            for small in Ticket.objects.filter(flight_no = model_to_dict(data)['flight_no']) :
                t.append(small)
            for smalll in model_to_dict(data)['crew']:
                c.append(smalll)
        
        a = model_to_dict(airport)['airplane']
        ag = model_to_dict(airport)['agency']
        flight_list = []
        ticket_list = []
        crew_list = []
        airplane_list = []
        agency_list = []

        for obj in f:
            flight_list.append(model_to_dict(obj))
        # print(flight_list)
        for obj in t:
            ticket_list.append(model_to_dict(obj))
        for obj in c:
            crew_list.append(model_to_dict(obj))
        for obj in a:
            airplane_list.append(model_to_dict(obj))
        for obj in ag:
            agency_list.append(model_to_dict(obj))
        
        print(flight_list)
        crew_list_1 = {new_list: [] for new_list in range(1000)}
        passenger_list = {new_list: [] for new_list in range(1000)}
        airplane_list_1 = {new_list: [] for new_list in range(1000)}
        counter = 0
        print("***********\n")
        for item in flight_list:
            print(item)
            context['flight'].append(item)
            for data in item['crew']:
                crew_list_1[counter].append(model_to_dict(data))
            
            for data1 in item['airplane']:
                airplane_list_1[counter].append(model_to_dict(data1))

            for data2 in item['passenger']:
                passenger_list[counter].append(model_to_dict(data2))
            counter += 1
        for i in range(len(context['flight'])):
            context['flight'][i]['crew'] = crew_list_1[i]
            context['flight'][i]['airplane'] = airplane_list_1[i]
            context['flight'][i]['passenger'] = passenger_list[i]

        print("********************\n")

        context['ticket'] = ticket_list
        context['crew'] = crew_list
        context['airplane'] = airplane_list
        context['agency'] = agency_list

        print(context)
    return HttpResponse(template.render({}, request))

@csrf_exempt 
def addNewAirport(request):
    template = loader.get_template('index/addNewAirport.html')
    template_name = 'index/addNewAirport.html'

    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        airplane = request.POST.get('airplane')
        agency = request.POST.get('agency')
        a = Airport(name=name, city=city, airplane=airplane, agency=agency)    
        a.save()
    return render(request, template_name, {})


def crew(request):
    template = loader.get_template('index/airportCrewTeam.html')
    # context = {'data': []}
    obj = Crew.objects.all()
    
    crew_data = []
    for item in obj:
        serialized_obj = model_to_dict(item)
        crew_data.append(serialized_obj)

    context = {'data': crew_data}
    print("hereee")
    print(context)
    return HttpResponse(template.render(context, request))



@csrf_exempt 
def addNewCrew(request):
    template = loader.get_template('index/addNewPeople.html')
    template_name = 'index/addNewPeople.html'

    if request.method == 'POST':
        print("POST")
        name = request.POST.get('name')
        family_name = request.POST.get('family_name')
        # gender = request.POST.get('gender')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        height = request.POST.get('height')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        profile_photo = request.POST.get('profile_photo')
        pilot_or_not = request.POST.get('pilot_or_not')
        new = Crew(name=name, family_name=family_name, email=email, user_name=user_name, password=password,
         height=height, phone_number=phone_number, address=address, profile_photo=profile_photo, pilot_or_not=pilot_or_not)
        print(new)
        new.save()
    return render(request, template_name, {})


def aircraft(request):
    template = loader.get_template('index/airportAircraft.html')
    # context = {'data': []}
    obj = Aircraft.objects.all()
    
    aircraft_data = []
    for item in obj:
        serialized_obj = model_to_dict(item)
        aircraft_data.append(serialized_obj)

    context = {'data': aircraft_data}
    print(context)
    return HttpResponse(template.render(context, request))



@csrf_exempt 
def addNewAircraft(request):
    template = loader.get_template('index/addNewAircraft.html')
    template_name = 'index/addNewAircraft.html'

    if request.method == 'POST':
        model = request.POST.get('model')
        capacity = request.POST.get('capacity')
        a = Aircraft(model=model, capacity=capacity)
        a.save()
    return render(request, template_name, {})
