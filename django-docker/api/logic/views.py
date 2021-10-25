from django.shortcuts import render

from rest_framework import viewsets

from logic import models, serializers


class AgentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing agent instances.
    """
    serializer_class = serializers.AgentSerializer
    queryset = models.Agent.objects.all()
