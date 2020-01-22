from rest_framework import serializers
from .models import Exam,Questions,ExamQuestion

class QuestionSerializer(serializers.ModelSerializer):
    text=serializers.CharField(max_length=500,read_only=True)
    c1 = serializers.CharField(max_length=500, read_only=True)
    c2 = serializers.CharField(max_length=500,read_only=True)
    c3 = serializers.CharField(max_length=500, read_only=True)
    c4 = serializers.CharField(max_length=500, read_only=True)

    class Meta:
        model=Questions
        fields=('text','c1','c2','c3','c4')




class ExamViewSerializer(serializers.ModelSerializer):

    questions=QuestionSerializer(read_only=True,many=True)

    # def get_questions(self,obj):
    #     orderd_questions=ExamQuestion.objects.filter(exam__id=obj.id)
    #     return QuestionSerializer(orderd_questions,many=True)
    class Meta:
        model=Exam
        fields=('id','date','done','score','questions')

