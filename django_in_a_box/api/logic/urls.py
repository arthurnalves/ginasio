from django.urls import path
from rest_framework.routers import DefaultRouter

from logic import views


router = DefaultRouter()
router.register(r'agent', views.AgentViewSet)
router.register(r'environment', views.EnvironmentViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = router.urls
