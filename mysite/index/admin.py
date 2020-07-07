from django.contrib import admin
from index.models import Flight, Passenger, Ticket, Agency, Airport, Crew
# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(Agency)
admin.site.register(Airport)
admin.site.register(Crew)