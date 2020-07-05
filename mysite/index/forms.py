from django import forms

class FlightForm(forms.Form):
    flight_no = forms.IntegerField()
    s_city = forms.CharField(max_length=100)
    d_city = forms.CharField(max_length=100)
    time_1 = forms.DateField()
    time_2 = forms.DateField()
    capacity = forms.IntegerField()


# class Ticket()