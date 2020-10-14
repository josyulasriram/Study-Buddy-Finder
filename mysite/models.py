# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
 
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
 



