# Generated by Django 4.2.3 on 2023-07-31 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_timetable_first_hour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.staffregistration'),
            preserve_default=False,
        ),
    ]
