from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    STRENGTH_CHOICES = (
        ('--------', '--------'),
        ('Mathematics','Mathematics'),
        ('Chemistry','Chemistry'),
        ('Physics','Physics'),
        ('Computer Science','Computer Science'),
        ('Economics','Economics'),
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100, blank=False, default='')
    strengths = models.CharField(max_length=255, choices = STRENGTH_CHOICES, default='')
    weaknesses = models.CharField(max_length=255, choices = STRENGTH_CHOICES, default='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Person(models.Model):
    STRENGTH_CHOICES = (
        ('Mathematics','Mathematics'),
        ('Chemistry','Chemistry'),
        ('Physics','Physics'),
        ('Computer Science','Computer Science'),
        ('Economics','Economics'),
        )
    name = models.CharField(max_length=100, blank=False)
    strengths = models.CharField(max_length=255, choices = STRENGTH_CHOICES)
    skills = models.CharField(max_length=255, blank=False)
    schedule = models.FileField(upload_to='schedules/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
