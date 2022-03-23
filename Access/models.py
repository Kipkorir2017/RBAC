from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200)
    JobNo=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name
        

class Department(models.Model):
    name=models.CharField(max_length=200)
    Flournum=models.AutoField(max_length=3)
    def __str__(self):
        return self.name


