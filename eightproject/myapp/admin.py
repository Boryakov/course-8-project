from django.contrib import admin

from .models import *
# admin user credentials: username : admin , password : lemon@789!


admin.site.register(Menu)
admin.site.register(Booking)
