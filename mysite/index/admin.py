from django.contrib import admin
from index.models import Flight, Passenger, Ticket
# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Ticket)