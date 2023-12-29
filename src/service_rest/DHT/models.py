from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import requests
import vonage
import telepot

class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)



