from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    OWNERSHIP_CHOICES = (
        ('Leased', 'Leased'),
        ('Owned', 'Owned'),
        )
    ownership = models.CharField(max_length=100, blank=True, null=True, choices = OWNERSHIP_CHOICES)
    area = models.FloatField(blank=True, null=True)
    gps = models.CharField(max_length=100, blank=True, null=True)
    CATEGORY_CHOICES = (
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial')
    )
    category = models.CharField(max_length=100, blank=True, null=True, choices = CATEGORY_CHOICES)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    street_name = models.CharField(max_length=100, blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_telephone = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Donor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    acronym = models.CharField(max_length=50, blank=True, null=True)
    CATEGORY_CHOICES = (
        ('Individual', 'Individual'),
        ('Government', 'Government'),
        ('NGO', 'NGO'),
        ('For Profit', 'For Profit'),
        ('Inter-Governmental', 'Inter-Governmental'),
        ('Diplomatic Missions', 'Diplomatic Missions'),
    )
    category = models.CharField(max_length=100, blank=True, null=True, choices = CATEGORY_CHOICES)
    plot_no = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    street_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_telephone = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
