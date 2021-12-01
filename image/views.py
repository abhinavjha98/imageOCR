from django.shortcuts import render
# EDA Packages
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
import requests
import easyocr
from PIL import Image
from django.core.files.storage import default_storage
# Create your views here.
class ImageText(viewsets.ViewSet):
    def getImage(self,request):
        reader = easyocr.Reader(['en'])
        file = request.data['file']
        file_name = default_storage.save('image/images/'+file.name, file)
# file extension (get the las 4 chars)
        file = default_storage.open(file_name)
        # handle file extension
        file_url = default_storage.url(file_name)
        result = reader.readtext(file_url,detail = 0, paragraph=False)
        print(result)
        imageMessage="";
        for x in result:
            imageMessage += ' '+x
        return Response(data={'message': imageMessage}, status=status.HTTP_200_OK)