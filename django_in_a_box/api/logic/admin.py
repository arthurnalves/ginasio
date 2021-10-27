from django.contrib import admin

from logic import models
from core import admin_mixins


@admin.register(models.Agent)
class AgentAdmin(
    admin_mixins.TrainAdminMixin,
    admin.ModelAdmin):
    list_display = ('pk', 'env_name', 'agent_actions',)

    def env_name(self, obj):
        return obj.environment.name


@admin.register(models.Data)
class DataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    pass