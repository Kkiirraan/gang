# Generated by Django 4.2.2 on 2023-06-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studenttimetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
