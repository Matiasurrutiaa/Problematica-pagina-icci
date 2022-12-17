# Generated by Django 4.1.4 on 2022-12-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('owner', models.CharField(max_length=500)),
                ('publication_date', models.DateField()),
                ('delete_at', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('rut', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('delete_at', models.BooleanField()),
            ],
        ),
    ]