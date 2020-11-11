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
    SCHEDULE_CHOICES = [
        ("Monday Morning", "Monday Morning"),
        ("Monday Afternoon", "Monday Afternoon"),
        ("Tuesday Morning", "Tuesday Morning"),
        ("Tuesday Afternoon", "Tuesday Afternoon"),
        ("Wednesday Morning", "Wednesday Morning"),
        ("Wednesday Afternoon", "Wednesday Afternoon"),
        ("Thursday Morning", "Thursday Morning"),
        ("Thursday Afternoon", "Thursday Afternoon"),
        ("Friday Morning", "Friday Morning"),
        ("Friday Afternoon", "Friday Afternoon"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100, blank=False, default='')
    meetingURL = models.CharField(max_length=100, blank=False, default='')
    strengths = models.CharField(
        max_length=255,
        choices=STRENGTH_CHOICES,
        default='')

    weaknesses = models.CharField(
        max_length=255,
        choices=STRENGTH_CHOICES,
        default='')

    availability = models.CharField(
        max_length=50,
        choices=SCHEDULE_CHOICES,
        default='Monday Morning',
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
