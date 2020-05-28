from django.db import models
class Studentresume(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mail = models.EmailField(max_length=150)
    phno = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    dist = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    pin = models.CharField(max_length=10)
    education = models.CharField(max_length=150)
    wstatus = models.CharField(max_length=150)
    skill = models.CharField(max_length=150)
    exp = models.CharField(max_length=100)
class Meta:
    db_table='studres'


# Create your models here.
