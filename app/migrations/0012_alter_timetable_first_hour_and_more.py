# Generated by Django 4.2.2 on 2023-06-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_staffregistration_subcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='first_hour',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='fourth_hour',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='second_hour',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='third_hour',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
