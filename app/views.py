from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


from .serializers import *
from .models import *


def error_bad_status():
    return Response({"ERROR": "ICORRECT REQUEST"}, status.HTTP_400_BAD_REQUEST)


def get_data(amount, some_model, some_serialaizer):
    match(amount):
        case "singular":
            instance = some_model
            serialized_instance = some_serialaizer(instance).data
            return Response(serialized_instance, status.HTTP_200_OK)
        
        case "plural":
            instances = some_model.objects.all()
            serialized_instance_list = some_serialaizer(instances, many=True).data
            return Response(serialized_instance_list, status.HTTP_200_OK)
        
        case _:
            error_bad_status()


def post_data(req, some_model, some_serialaizer):
    try:
        some_model.objects.create(**req.data)
        
        return Response(some_serialaizer(some_model.objects.all(), many=True).data)
    
    except:
        error_bad_status()
    
    
def put_data(req, arg, some_model, some_serialaizer):
    try:
        old_model_object = some_model.objects.get(id=arg)
        some_serialaizer(old_model_object, data=req.data, partial=False).save
        
        return Response(some_serialaizer(some_model.objects.all(), many=True).data)
    
    except:
        error_bad_status()
        
        
def delete_data(arg, some_model, some_serialaizer):
    try:
        old_model = some_model.objects.get(id=arg)
        old_model.delete()
        
        return Response(some_serialaizer(some_model.objects.all(), many=True).data)
    
    except:
        error_bad_status()
    
    
class Movies(ViewSet):
    def movies(self, req):
        try:
            return get_data('plural', req, Movie, SerializedMovie)
        except:
            error_bad_status()
        
    def movie(self, req, arg):
        try:
            return get_data('singular', Movie.objects.get(id=arg), SerializedMovie)
        except:
            error_bad_status()
            
    def create_movie(self, req):
        return post_data(req, Movie, SerializedMovie)

    def delete_movie(self, req, arg):
        return delete_data(arg, Movie, SerializedMovie)

    def put_movie(self, req, arg):
        return put_data(req, arg, Movie, SerializedMovie)

class Tickets(APIView):
    def get(self, req, arg):
        try:
            return get_data('singular', Ticket.objects.get(id=arg), SerializedTicket)
        except:
            error_bad_status()
    
    def post(self, req):
        return post_data(req, Ticket, SerializedTicket)
    
    def delete(self, req, arg):
        return delete_data(arg, Ticket, SerializedTicket)
        
        
@api_view(['GET', 'POST'])
def users(req):
    if req.method == 'GET':
        try:
            return get_data('plural', req, User, UserSerializer)
        except:
            error_bad_status()
    
    elif req.method == 'POST':
        return post_data(req, User, UserSerializer)
        
    else:
        error_bad_status()


@api_view(['GET', 'PUT', 'DELETE'])
def user(req, arg):
    if req.method == 'GET':
        try:
            return get_data('singular', User.objects.get(id=arg), UserSerializer)
        except:
            error_bad_status()
        
    elif req.method == 'PUT':
        return put_data(req, arg, Movie, SerializedMovie)
        
    elif req.method == 'DELETE':
        return delete_data(arg, User, UserSerializer)

    else:
        error_bad_status()


class Places:
    @staticmethod
    @api_view(['GET', 'POST'])
    def places(req):     
        if req.method == 'GET':
            try:
                return get_data('plural', req, Place, SerializedPlace)
            except:
                error_bad_status()
        
        elif req.method == 'POST':
            return post_data(req, Place, SerializedPlace)
        
        else:
            error_bad_status()
            
    @staticmethod
    @api_view(['GET', 'DELETE'])
    def place(req, arg):     
        if req.method == 'GET':
            try:
                return get_data('singular', Place.objects.get(id=arg), SerializedPlace)
            except:
                error_bad_status()
            
        elif req.method == 'DELETE':
            return delete_data(arg, Place, SerializedPlace)
        
        else:
            error_bad_status()