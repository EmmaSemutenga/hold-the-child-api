from rest_framework import serializers
from .models import Project, WorkPlan, MileStone, Supply, Travel

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'name', 'donor', 'program', 'location', 'amount', 'start_date', 'end_date', 'overral_strategy', 'donor_agreement', 'status')

class WorkPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkPlan
        fields = ('url', 'project', 'activity', 'description')

class MilestoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MileStone
        fields = ('url', 'work_plan', 'indicator', 'target', 'duration', 'cost')

class SupplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supply
        fields = ('url', 'project', 'name', 'units', 'value', 'vendor')

class TravelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Travel
        fields = ('url', 'project', 'travel_role', 'travel_type', 'reason', 'start_date', 'end_date')