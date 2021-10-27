from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin

class TrainAdminMixin:
    def agent_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Train</a>',
            reverse('agent-detail', args=[obj.pk])
        )
    agent_actions.allow_tags = True
    agent_actions.short_description = "Actions"

    