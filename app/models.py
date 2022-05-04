from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Marks(models.Model):
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    PhysicsMarks = models.IntegerField(null=True)
    ChemistryMarks  = models.IntegerField(null=True)
    MathsMarks  = models.IntegerField(null=True)
    EnglishMarks  = models.IntegerField(null=True)
    ComputerMarks  = models.IntegerField(null=True)

    def __str__(self):
        return self.StudentName


