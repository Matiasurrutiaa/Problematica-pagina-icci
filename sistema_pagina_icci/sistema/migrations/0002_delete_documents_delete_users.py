# Generated by Django 4.1.4 on 2022-12-17 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
