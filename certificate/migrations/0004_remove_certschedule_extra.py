# Generated by Django 3.1.2 on 2020-11-09 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_auto_20201109_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certschedule',
            name='extra',
        ),
    ]
