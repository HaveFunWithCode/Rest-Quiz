from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    scores=models.IntegerField(default=0)
    birth_date=models.DateField(null=True)





