from rest_framework import serializers
from .models import Location, Donor, Vendor

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ("url", "name", "ownership", "area", "gps", "category", "block_name", "street_name", "city_name", "country", "contact_person", "contact_telephone", "email_address")

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ("url", "name", "acronym", "category", "plot_no", "block_name", "street_name", "city", "country", "contact_person", "contact_telephone", "email_address")

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ("url", "name")