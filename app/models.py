from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Marks(models.Model):
    StudentName = models.CharField(max_length=200,null=True)
    # id = models.AutoField(primary_key=True)
    StudentId  = models.CharField(primary_key=True,max_length=50)
    PhysicsMarks = models.IntegerField(null=True)
    ChemistryMarks  = models.IntegerField(null=True)
    MathsMarks  = models.IntegerField(null=True)
    EnglishMarks  = models.IntegerField(null=True)
    LanguageMarks  = models.IntegerField(null=True)

    def __str__(self):
        return self.StudentName


