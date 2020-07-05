from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import loader

def main(request):
    template = loader.get_template('index/myindex.html')
    context = {
        'data': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))

def flights(request):
    template = loader.get_template('index/airportFlights.html')
    # context = query
    return HttpResponse(template.render(context, request))

def tickets(request):
    pass
