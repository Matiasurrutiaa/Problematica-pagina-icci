# Generated by Django 4.1.4 on 2022-12-19 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='author',
            field=models.CharField(max_length=500, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='delete_at',
            field=models.BooleanField(verbose_name='inactivo'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='owner',
            field=models.CharField(max_length=500, verbose_name='Dueño'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='publication_date',
            field=models.DateField(verbose_name='Fecha de Publicación'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='users',
            name='delete_at',
            field=models.BooleanField(verbose_name='inactivo'),
        ),
        migrations.AlterField(
            model_name='users',
            name='dv',
            field=models.CharField(max_length=1, verbose_name='Digito Verificador'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=10, verbose_name='Contraseña'),
        ),
    ]