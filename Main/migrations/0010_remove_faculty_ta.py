# Generated by Django 3.0.5 on 2022-06-16 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_faculty_ta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='ta',
        ),
    ]
