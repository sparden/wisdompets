from django.db import models

class Pet(models.Model):
    SEX_CHOICES=[('M','Male'),('F','Female')]
    name=models.CharField(max_length=100) 
    submitter=models.CharField(max_length=100) 
    species=models.CharField(max_length=30) 
    breed=models.CharField(max_length=30, blank=True)
    description=models.TextField(blank=True)#textfield is used so that string length will no longer be required
    sex=models.CharField(max_length=1, blank=True, choices=SEX_CHOICES)
    submission_date=models.DateTimeField()
    age=models.IntegerField(null= True)
    vaccinations=models.ManyToManyField('Vaccine', blank=True)#blank=true is used so that field will not be required anymore
      
class Vaccine(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self): 
        return self.name