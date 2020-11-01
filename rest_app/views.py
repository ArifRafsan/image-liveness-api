from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from rest_framework import status
import base64
import logging
from eye.eye2 import blink_count
from datetime import date
from .forms import UserForm
from django.http import HttpResponse
import json
from datetime import datetime


def showHome(request):
    return render(request, 'home.html')


@api_view(['POST'])
def process_form(request):
    if request.method == 'POST':
        user = UserForm(request.POST, request.FILES)
        if user.is_valid():
            f = request.FILES['file']
            name = f.name
          
            with open('media/videos/' + name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            # video to image
            path = "media/videos/"
            video = path + name
            total_count = blink_count(video)

            #image to base64
            image_name = name + '.jpg'
            image = open(path + image_name, 'rb')
            image_read = image.read()
            image_64_encode = base64.encodestring(image_read)

            time = datetime.now()
            timestamp = time.strftime("%d/%m/%Y %H:%M:%S")

            s201 = status.HTTP_201_CREATED
            
            #json
            data = {"status": s201,"timestamp": timestamp,"totalcount": total_count, "img_string": image_64_encode}

            return Response(data)
        return Response(user.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
