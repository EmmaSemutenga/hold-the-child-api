from django.shortcuts import render
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework import viewsets

# Create your views here.
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer