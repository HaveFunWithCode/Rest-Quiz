from django.utils import timezone

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Questions,Exam
from .serializers import ExamViewSerializer
class quizHomeAPIView(APIView):
    permission_classes =[IsAuthenticated]

    def get(self,request):
        token=request.META.get('HTTP_AUTHORIZATION').replace('Token','').strip()
        user=User.objects.get(id=Token.objects.get(key=token).user_id)

        exam = Exam(user=user, date=timezone.now(), answers='', score=0)
        exam.save()
        questions=Questions.objects.order_by('?')[0:5]
        for q in questions:
            exam.questions.add(q)

        return Response({'examid':exam.id})

class quizExamAPIView(APIView):

    def get(self,request,exam_id=None):
        exam=Exam.objects.get(id=exam_id)
        serializer=ExamViewSerializer(exam)
        return Response(serializer.data)

    def post(self,request,exam_id=None):
        return Response({'mess':'ok'})


