from django.contrib import admin
from django.urls import path, include
from .views import quizHomeAPIView,quizExamAPIView


urlpatterns = [
    path('', quizHomeAPIView.as_view()),
    path('exam/<int:exam_id>', quizExamAPIView.as_view()),
]
