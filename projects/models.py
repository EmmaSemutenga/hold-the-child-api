from django.db import models
from operations.models import Donor, Location, Vendor
from programs.models import Program

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    overral_strategy = models.TextField(blank=True, null=True)
    donor_agreement = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, blank=True, null=True )

    def __str__(self):
        return self.name
    
#workplan and milestone to be on one form    
class WorkPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    activity = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.activity


class MileStone(models.Model):
    work_plan = models.ForeignKey(WorkPlan, on_delete=models.CASCADE, blank=True, null=True)
    indicator = models.CharField(max_length=100, blank=True, null=True)
    target = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.indicator
#workplan and milestone to be on one form 


class Supply(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    units = models.PositiveIntegerField(blank=True, null=True)
    value = models.PositiveIntegerField(blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.name

#Teams--waiting for xd schema
class Travel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    travel_role = models.CharField(max_length=100, blank=True, null=True)
    travel_type = models.CharField(max_length=100, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.travel_role
