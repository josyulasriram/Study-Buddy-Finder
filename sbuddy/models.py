
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    strengths = models.CharField(max_length=255, blank=False)
    skills = models.CharField(max_length=255, blank=False)
    schedule = models.FileField(upload_to='schedules/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
