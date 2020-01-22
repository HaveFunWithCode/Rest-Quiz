from django.contrib import admin
from django.urls import path, include
from .views import SignUpAPIView,LoginAPIView
from rest_framework.authtoken import views as rest_framework_views

from rest_framework.routers import DefaultRouter, SimpleRouter

# router =DefaultRouter()
# router.register('helloo',HelloViewSet,basename='helloviewset')
#
#
urlpatterns = [
    path('signup/',SignUpAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    # path('logout/',SignUpAPIView.as_view()),
    # path('get_auth_token/',rest_framework_views.obtain_auth_token,name='get_auth_token'),
]
