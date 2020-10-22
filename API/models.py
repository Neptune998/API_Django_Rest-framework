from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=60)
    hospital = models.CharField(max_length=60)
    contact = models.IntegerField()
    date = models.DateField()

 
    def __str__(self):
        return self.name
