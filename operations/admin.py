from django.contrib import admin

from .models import Donor, Location, Vendor

# Register your models here.
admin.site.register(Donor)
admin.site.register(Location)
admin.site.register(Vendor)