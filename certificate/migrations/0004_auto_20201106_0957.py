# Generated by Django 3.1.2 on 2020-11-06 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_certschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='cost_sil',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='examinee_sil',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='pass_percent_sil',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='cost',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='examinee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='pass_percent',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]