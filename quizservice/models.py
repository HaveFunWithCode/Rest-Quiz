from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Questions(models.Model):
    text=models.CharField(max_length=500)
    c1=models.CharField(max_length=400,null=False)
    c2=models.CharField(max_length=400,null=False)
    c3=models.CharField(max_length=400,null=False)
    c4=models.CharField(max_length=400,null=False)
    correct_choice_id=models.IntegerField(default=1,
                                          validators=[RegexValidator(
                                              regex='^[1-4]$',
                                              message='You should Choice number between 1 to 4 only'
                                          ),])
    def __str__(self):
        return self.text


class Exam(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField()
    questions=models.ManyToManyField(Questions,through='ExamQuestion')

    answers=models.CharField(max_length=500,default="")
    score = models.FloatField(default=0)
class ExamQuestion(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
