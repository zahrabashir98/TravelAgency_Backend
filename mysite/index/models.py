from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_no = models.IntegerField()
    s_city = models.CharField(max_length=100)
    d_city = models.CharField(max_length=100)
    time_1 = models.DateField()
    time_2 = models.DateField()
    capacity = models.IntegerField()

    # pilot 
    # crew
    # airplane
    # passenger = models.ManyToManyField('Passenger')
    # def __str__(self):
    #     return self.flight_no


TITLE_CHOICES = [
    ('Female', 'female'),
    ('Male', 'male'),
]


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    famly_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=TITLE_CHOICES)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    flight = models.ManyToManyField('Flight')
    
    # def __str__(self):
    #     return self.name

class Ticket(models.Model):

    flight_no = models.IntegerField()
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    # flight = Flight.objects.get(flight_no=int(flight_no))