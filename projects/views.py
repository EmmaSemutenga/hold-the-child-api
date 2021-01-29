from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, WorkPlan, MileStone, Supply, Travel
from .serializers import ProjectSerializer, WorkPlanSerializer, MilestoneSerializer, SupplySerializer, TravelSerializer
# Create your views here.

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class WorkplanViewset(viewsets.ModelViewSet):
    queryset = WorkPlan.objects.all()
    serializer_class = WorkPlanSerializer

class MileStoneViewset(viewsets.ModelViewSet):
    queryset = MileStone.objects.all()
    serializer_class = MilestoneSerializer

class SupplyViewset(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

class TravelViewset(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
