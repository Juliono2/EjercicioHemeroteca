from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'', views.AreaViewSet, basename='area')

urlpatterns = [
]

urlpatterns = urlpatterns + router.urls