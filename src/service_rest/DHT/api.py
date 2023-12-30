
########
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dht11
from .serializers import DHT11serialize
import requests
import vonage
import telepot

# Initialize a global counter variable
person_counter = 0

@api_view(["GET", "POST"])
def dhtser(request):
    global person_counter

    if request.method == "GET":
        all = Dht11.objects.all()
        dataSer = DHT11serialize(all, many=True)
        return Response(dataSer.data)
    elif request.method == "POST":
        serial = DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            if Dht11.objects.last().temp > 30:
                if person_counter == 0:
                    subject = 'Alerte DHT'
                    message = f'Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list =['ibrahimlahlou021@gmail.com']
                    send_mail(subject, message, email_from, recipient_list)
                    ######
                    26173672
                    base_url = f'https://api.telegram.org/bot6977845764:630ebf07e5b7334718f3aadf67cc4fc9/sendMessage?chat_id=-26173672&text="la temperature est {Dht11.objects.last().temp} et depassé la limite"'
                    requests.get(base_url)
                    ##############
                    client = vonage.Client(key="45529cbe", secret="1YTJ34aik98vCkL0")
                    client.sms.send_message(
                        {
                            "from": "Alerte",
                            "to": "212654849412",
                            "text": f"Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.",
                        })
                    #####################
                elif person_counter == 1:
                    subject = 'Alerte DHT'
                    message = f'Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['ibrahimlahlou021@gmail.com']
                    send_mail(subject, message, email_from, recipient_list)
                    ######
                    base_url = f'"la temperature est {Dht11.objects.last().temp} et depassé la limite"'
                    requests.get(base_url)
                    ##############
                    client = vonage.Client(key="21fa3bd8", secret="JesgGuzv39K3FtVD")
                    client.sms.send_message(
                        {
                            "from": "Alerte",
                            "to": "212682405510",
                            "text": f"Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.",
                        })

                else:
                    subject = 'Alerte DHT'
                    message = f'Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['ibrahimlahlou021@gmail.com']
                    send_mail(subject, message, email_from, recipient_list)
                    ######
                    base_url = f'"la temperature est: {Dht11.objects.last().temp}  et depassé la limite"'
                    requests.get(base_url)
                    base_url1 = f'"la temperature est {Dht11.objects.last().temp} et depassé la limite"'
                    requests.get(base_url1)
                    ##############
                    client = vonage.Client(key="45529cbe", secret="1YTJ34aik98vCkL0")
                    client.sms.send_message(
                        {
                            "from": "Alerte",
                            "to": "212654849412",
                            "text": f"Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.",
                        })
                    client2 = vonage.Client(key="21fa3bd8", secret="JesgGuzv39K3FtVD")
                    client2.sms.send_message(
                        {
                            "from": "Alerte",
                            "to": "212682405510",
                            "text": f"Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.",
                        })
                    #####################
                person_counter += 1

            if Dht11.objects.last().temp < 30:
                person_counter = 0
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.id, status=status.HTTP_400_CREATED)







