from django.contrib import admin
from .models import Project, WorkPlan, MileStone, Supply, Travel
# Register your models here.
admin.site.register(Project)
admin.site.register(WorkPlan)
admin.site.register(MileStone)
admin.site.register(Supply)
admin.site.register(Travel)
