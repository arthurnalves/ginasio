from rest_framework import serializers

from logic import models


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = '__all__'
