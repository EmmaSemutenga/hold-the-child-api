from django.contrib import admin

from .models import Indicator, ManagementApproach, MileStone, Program, ProgrammaticApproach
# Register your models here.
admin.site.register(Indicator)
admin.site.register(ManagementApproach)
admin.site.register(MileStone)
admin.site.register(Program)
admin.site.register(ProgrammaticApproach)
