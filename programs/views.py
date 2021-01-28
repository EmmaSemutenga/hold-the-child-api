from django.shortcuts import render
from .models import Program, ProgrammaticApproach, Indicator, ManagementApproach, MileStone
from .serializers import ProgramSerializer, ProgrammaticApproachSerializer, IndicatorSerializer, ManagementApproachSerializer, MileStoneSerializer
from rest_framework import viewsets
# Create your views here.

class ProgramViewset(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ProgrammaticApproachViewset(viewsets.ModelViewSet):
    queryset = ProgrammaticApproach.objects.all()
    serializer_class = ProgrammaticApproachSerializer

class IndicatorViewset(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

class ManagementApproachViewset(viewsets.ModelViewSet):
    queryset = ManagementApproach.objects.all()
    serializer_class = ManagementApproachSerializer

class MileStoneViewset(viewsets.ModelViewSet):
    queryset = MileStone.objects.all()
    serializer_class = MileStoneSerializer