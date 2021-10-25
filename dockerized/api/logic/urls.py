from django.urls import path
from rest_framework.routers import DefaultRouter

from logic import views


router = DefaultRouter()
router.register(r'agents', views.AgentViewSet)

urlpatterns = router.urls
