from django.db import models

# Create your models here.
class Marks(models.Model):
    Rollno=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Sub1=models.FloatField()
    Sub2=models.FloatField()
