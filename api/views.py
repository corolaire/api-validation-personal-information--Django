from django.shortcuts import render
from rest_framework import viewsets
from .serializer import serializeruser,serializerprofile
#importa los serializadore y debajo importa el modelo(en mi caso son varios modelos)
from .models import profile,user


class userViewSet(viewsets.ModelViewSet):#aca desarrollamos el query set , vamos a acceder a los elementos mediante la orm de django.
    queryset=user.objects.all() #los enlista para poder acceder a los elementos de una tabla
    serializer_class=serializeruser
    
class profileViewSet(viewsets.ModelViewSet):
    queryset=profile.objects.all()
    serializer_class=serializerprofile
# Create your views here.
