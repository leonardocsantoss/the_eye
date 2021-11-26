from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from core.models import Application
from core.serializers import ResponseSerializer, EventSerializer
from core.tasks import save_event


class EventView(generics.CreateAPIView):
    """
        API endpoint to save a new Event.
        
        This endpoint verifies if the request origin is valid, and creates a new Session if it does not exist.
    """
    serializer_class = EventSerializer

    _applications = {}
    def get_application(self, host):
        # Get the application using a class cache
        if not EventView._applications.get(host):
            try:
                application = Application.objects.get(host=host)
                EventView._applications[host] = application
            except Application.DoesNotExist:
                return None
        return EventView._applications.get(host)
    
    @swagger_auto_schema(responses={200: ResponseSerializer})
    def post(self, request, *args, **kwargs):
        
        # Verify if the host is valid using a class cache
        application = self.get_application(request.headers['Origin'])
        if not application:
            print(application)
            return Response({"status": False}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        validated_data['application_id'] = application.id

        # Save using Celery task to avoid blocking the request
        save_event.delay(validated_data=validated_data)
        return Response({"status": True}, status=status.HTTP_201_CREATED)
    