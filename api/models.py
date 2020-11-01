from django.conf import settings
from django.db import models

class StudyPlan(models.Model):
    content_id = models.CharField(max_length=50)

    class Meta:
        db_table = "study_plan"

    def __str__(self):
        return self.content_id


class User(models.Model):
    id_token = models.CharField(max_length=500)
    secret_key = models.CharField(max_length=500)
    interest = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

