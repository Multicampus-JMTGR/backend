# Generated by Django 3.1.2 on 2020-11-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyplan',
            name='content',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
