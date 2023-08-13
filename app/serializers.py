from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class SerializedMovie(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('label', 'image', 'description', 'slug')
        
        
class SerializedTicket(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('movie_id', 'price', 'owner', 'date')
        
        
class SerializedPlace(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('ticket_id', 'number')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']