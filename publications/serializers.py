from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ('url', 'title', 'document_type', 'publication_date', 'name_of_publisher', 'author', 'description', 'attachment')