from django.contrib import admin
from django.urls import path, include
from .views import SignUpAPIView

from rest_framework.routers import DefaultRouter, SimpleRouter

# router =DefaultRouter()
# router.register('helloo',HelloViewSet,basename='helloviewset')
#
#
urlpatterns = [
    path('signup/',SignUpAPIView.as_view()),
]
