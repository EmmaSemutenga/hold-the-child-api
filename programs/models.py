from django.db import models

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    goal = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    strategic_plan = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

#on same form
class ProgrammaticApproach(models.Model):
    program = models.OneToOneField(Program, on_delete = models.CASCADE, blank=True, null=True)
    theme_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.theme_title

class Indicator(models.Model):
    programmatic_approach = models.ForeignKey(ProgrammaticApproach, on_delete = models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    target = models.CharField(max_length=100, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

#on same form


#on same form
class ManagementApproach(models.Model):
    program = models.OneToOneField(Program, on_delete = models.CASCADE, blank=True, null=True)
    domain_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.domain_title

class MileStone(models.Model):
    management_approach = models.ForeignKey(ManagementApproach, on_delete=models.CASCADE, blank=True, null=True)
    indicator = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.indicator

#on same form