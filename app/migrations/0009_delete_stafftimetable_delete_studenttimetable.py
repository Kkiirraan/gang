# Generated by Django 4.2.2 on 2023-06-29 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StaffTimetable',
        ),
        migrations.DeleteModel(
            name='StudentTimetable',
        ),
    ]