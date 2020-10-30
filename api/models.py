from django.conf import settings
from django.db import models

class StudyPlan(models.Model):
    content_id = models.CharField(max_length=50)

    class Meta:
        db_table = "study_plan"

    def __str__(self):
        return self.content_id
