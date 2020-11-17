import os
from twilio.rest import Client
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

    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        if self.phone_number:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']#'ACcbf1b53b4f4f0d9bbb92a1304d3aaa76'os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']#'ec8302fef58f3ebf9ddead86fb8ea18d'#os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                                            body='Welcome to the Study Buddy App',
                                            from_='+13157549860',
                                            to=self.phone_number
                                             )


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                              body='Hi there!',
                              from_='+13157549860',
                              to='+15715999055'
                          )

            print(message.sid)
        return super().save(*args, **kwargs)

            
    