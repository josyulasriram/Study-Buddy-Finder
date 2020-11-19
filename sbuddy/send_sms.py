# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_ACCOUNT_SID = "AC5874e26480e8bb02c1d0d03bd7908283"
TWILIO_AUTH_TOKEN = "1fe94d62d5d7e0e9ec903e47b71965e8"
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_text(receiver, message):
    message = client.messages.create(
        body=message,
        from_='+15707553171',
        to=receiver
    )

