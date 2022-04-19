from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Score(models.Model):
    username=models.CharField(max_length=20)
    score=models.IntegerField(null=True)
    subjectName=models.CharField(max_length=10,null=True)


    def __str__(self):
        return self.username

    class Meta:
        ordering=['username']