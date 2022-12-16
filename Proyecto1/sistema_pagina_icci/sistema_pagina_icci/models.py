from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    rut=models.IntegerField()
    mail=models.EmailField()
    password=models.CharField(max_length=10)
    delete_at=models.BooleanField()

class Documents(models.Model):
     url=models.URLField()
     description=models.TextField()
     title=models.CharField(max_length=500)
     author=models.CharField(max_length=500)
     owner=models.CharField(max_length=500)
     publication_date=models.DateField()
     delete_at=models.BooleanField()
     

 
         