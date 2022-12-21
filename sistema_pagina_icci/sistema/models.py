from django.db import models

# Create your models here.


class Documents(models.Model):
     url=models.URLField()
     description=models.TextField( blank=True, null=True, verbose_name="Descripción")
     title=models.CharField(max_length=500, verbose_name="Título")
     author=models.CharField(max_length=500, verbose_name="Autor")
     owner=models.CharField(max_length=500, blank=True, null=True ,verbose_name="Dueño")
     publication_date=models.DateField(verbose_name="Fecha de Publicación")
     delete_at=models.BooleanField(verbose_name="inactivo")

     #def __str__(self):
      #    return self.title