from rest_framework import serializers
from .models import profile,user

class serializerprofile(serializers.ModelSerializer): 
    class Meta:
        model=profile #modelo con el cual vamos a trabajar
        fields=['name','lastname','phonenumber','age','gender','nationality']# campos (columnas a mi entender)django genera automatic.pk a los campos
        # el id pk esta en la base de datos directamente con django
        
class serializeruser(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['name','email','password']