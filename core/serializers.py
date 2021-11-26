from rest_framework import serializers
from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp',]

    session_id = serializers.CharField(required=True, max_length=36)


class ResponseSerializer(serializers.Serializer):
    
    status = serializers.BooleanField(required=True)