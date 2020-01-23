import json

from django.utils import timezone

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import Questions,Exam
from .serializers import ExamViewSerializer, ExamListSerializer, ExamDetailSerializer


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


class CustomPagination(PageNumberPagination):
    page_size = 5

# class quizExamViewSet(ReadOnlyModelViewSet):
#     queryset = Exam.objects.all()
#     # pagination_class = CustomPagination
#     serializers = {
#         'list': ExamListSerializer,
#         'retrieve': ExamDetailSerializer
#     }
#
#     def get_serializer_class(self):
#         return self.serializers.get(self.action)
# TODO: put permission limit on this view and give permition just to user who have this exam
class quizExamViewSet(ModelViewSet):
    # pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    serializers = {
        'list': ExamListSerializer
    }

    def get_queryset(self):
        queryset = Exam.objects.filter(user=self.request.user)
        return queryset


    def get_serializer_class(self):
        return self.serializers.get(self.action)





# TODO: put permission limit on this view and give permition just to user who have this exam
class quizExamAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        exam=Exam.objects.get(id=id)
        serializer=ExamViewSerializer(exam)
        return Response(serializer.data)



    def post(self,request,id=None):

        json_obj=json.loads(request.body.decode("utf-8"))
        examid=json_obj['examid']
        exam=Exam.objects.get(id=int(examid))
        if exam.done:
            return Response({'message':'You have Done this exam before'})
        else:
            keys=[q.correct_choice_id for q in exam.questions.all()]
            user_answers={}
            trues=0
            falses=0
            for answer in json_obj:
                if answer!='examid':
                    user_answers[answer]=json_obj[answer]
            for i,key in enumerate(keys):
                if str(i+1) in user_answers:
                    if int(user_answers[str(i+1)])==keys[i]:
                        trues+=1
                    else:
                        falses+=1
            result=((3*trues-falses)*100)/(3*5)
            # save and send  result
            exam.answers=str(user_answers)
            exam.score=str(round(result,2))
            exam.done=True
            exam.save()
            return Response({"Your Score is" : str(round(result,2))})



