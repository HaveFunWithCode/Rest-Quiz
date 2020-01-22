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

class QuestionSerializerAnswered(serializers.ModelSerializer):
    text=serializers.CharField(max_length=500,read_only=True)
    c1 = serializers.CharField(max_length=500, read_only=True)
    c2 = serializers.CharField(max_length=500,read_only=True)
    c3 = serializers.CharField(max_length=500, read_only=True)
    c4 = serializers.CharField(max_length=500, read_only=True)
    correct_choice_id=serializers.IntegerField(read_only=True)

    class Meta:
        model=Questions
        fields=('text','c1','c2','c3','c4','correct_choice_id')




class ExamViewSerializer(serializers.ModelSerializer):

    # questions=QuestionSerializer(read_only=True,many=True)
    questions=serializers.SerializerMethodField('get_questions')

    def get_questions(self,obj):
        questions = [q.question for q in ExamQuestion.objects.filter(exam__id=obj.id)]
        if obj.done:
            return QuestionSerializerAnswered(questions,read_only=True,many=True,context=self.context).data
        else:
            return QuestionSerializer(questions,read_only=True,many=True,context=self.context).data
    class Meta:
        model=Exam
        fields=('id','date','done','score','questions')


