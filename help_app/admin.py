from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Branch_user)
admin.site.register(Branch)
admin.site.register(Ticket_counter)
admin.site.register(Ticket)