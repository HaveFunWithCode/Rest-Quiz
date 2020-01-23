from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import quizHomeAPIView,quizExamAPIView,quizExamViewSet

routers=DefaultRouter()

# list all exam for authenticated user
routers.register('exam/list',quizExamViewSet,basename='examlist')

urlpatterns = [
    # start page after login and start an exam and return an examid which should be use in
    path('exam/', quizHomeAPIView.as_view()),
    # start exam
    path('exam/<int:id>', quizExamAPIView.as_view(),name='examdetail'),
    # path('exam/', quizExamViewSet.as_view()),
    # path('', include(routers.urls)),
]
urlpatterns+=routers.urls