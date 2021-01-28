from rest_framework import serializers
from .models import Program, ProgrammaticApproach, Indicator, ManagementApproach, MileStone

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ('url', 'title', 'country', 'goal', 'start_date', 'end_date', 'description', 'strategic_plan')

class ProgrammaticApproachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgrammaticApproach
        fields = ('url', 'program', 'theme_title', 'description')

class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicator
        fields = ('url', 'programmatic_approach', 'name', 'target', 'cost')

class ManagementApproachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManagementApproach
        fields = ('url', 'program', 'domain_title', 'description')

class MileStoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MileStone
        fields = ('url', 'management_approach', 'indicator', 'duration', 'cost')