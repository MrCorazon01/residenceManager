from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(ReservationModel)
admin.site.register(RoomModel)
admin.site.register(PaymentModel)
admin.site.register(ComplaintModel)
