from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


from .serializers import *
from .models import *


class Movies(ViewSet):
    def movies(self, req):
        try:

            movies = Movie.objects.all()
            serialized_movie_list = SerializedMovie(movies, many=True).data
            return Response(serialized_movie_list, status.HTTP_200_OK)
        except:
            return Response({"msg": "ICORRECT DATA"}, status.HTTP_400_BAD_REQUEST)
        
    def movie(self, req, arg):
        try:
            movie = Movie.objects.get(id=arg)
            serialized_movie = SerializedMovie(movie).data
            
            return Response(serialized_movie, status.HTTP_200_OK)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)
            
    def create_movie(self, req, arg):
        try:
            
            return Response({'msg': 'movie was successfuly created!'},
                            status.HTTP_201_CREATED)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)
        
    def delete_movie(self, req, arg):
        try:
            return Response({'msg': 'movie was delete!'},status.HTTP_200_OK)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)

    def put_movie(self, req, arg):
        try:
            return Response({'msg': 'movie was huyuting!'},status.HTTP_200_OK)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)


class Tickets(APIView):
    def get(self, req, arg):
        try:
            ticket = Ticket.objects.get(id=arg)
            serialized_ticket = SerializedTicket(ticket).data
            return Response(serialized_ticket, status.HTTP_200_OK)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)
    
    def post(self, req, arg):
        try:
            return Response({'msg': 'Ticket was successfuly added!'},
                            status.HTTP_201_CREATED)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)
    
    def delete(self, req, arg):
        try:
            return Response({'msg': 'HUCK YOU!'},status.HTTP_200_OK)
        except:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET', 'POST'])
def users(req):
    if req.method == 'GET':
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True).data
        return Response(serialized_users,status.HTTP_200_OK)
    
    elif req.method == 'POST':
        return Response({'msg': 'user was successfuly created!'},
                        status.HTTP_201_CREATED)
        
    else:
        return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user(req, arg):
    if req.method == 'GET':
        user = User.objects.get(id=arg)
        serialized_user = UserSerializer(user).data
        return Response(serialized_user, status.HTTP_200_OK)
    
    elif req.method == 'POST':
        return Response({'msg': 'user was successfuly created!'},
                        status.HTTP_201_CREATED)
        
    elif req.method == 'PUT':
        return Response({'msg': 'user`s data was chanched'},
                        status.HTTP_200_OK)
        
    elif req.method == 'DELETE':
        return Response({'msg': 'HUCK YOU!'},status.HTTP_200_OK)

    else:
        return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)


class Places:
    @staticmethod
    @api_view(['GET', 'POST'])
    def places(req):     
        if req.method == 'GET':
            places = Place.objects.all()
            serialized_places = SerializedPlace(places, many=True).data
            return Response(serialized_places, status.HTTP_200_OK)
        
        elif req.method == 'POST':
            return Response({'msg': 'place was holder by user!'},
                            status.HTTP_201_CREATED)
        else:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)
            
    @staticmethod
    @api_view(['GET', 'POST', 'DELETE'])
    def place(req, arg):     
        if req.method == 'GET':
            place = Place.objects.get(id=arg)
            serialized_place = SerializedPlace(place, many=True).data
            return Response(serialized_place, status.HTTP_200_OK)
        
        elif req.method == 'POST':
            return Response({'msg': 'place was holder by user!'},
                            status.HTTP_201_CREATED)
            
        elif req.method == 'DELETE':
            return Response({'msg': 'HUCK YOU!'},status.HTTP_200_OK)
        
        else:
            return Response({"msg": "ICORRECT DATA"},status.HTTP_400_BAD_REQUEST)