from django.urls import re_path as url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'circuit-construction', views.CircuitConstructionViewSet, basename='')
urlpatterns = [
    url('^$', views.hello),  # /api/
    url(r'^', include(router.urls)),  # /api/circuit-construction/construct   /api/circuit-construction/test
]