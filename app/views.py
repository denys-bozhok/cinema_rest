from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics


from .serializers import *
from .models import *


def error_bad_status():
    return Response({"ERROR": "ICORRECT REQUEST"}, status.HTTP_400_BAD_REQUEST)


def post_data(req, some_model, some_serialaizer):
    print(req.data)
    some_model.objects.create(**req.data)
    return Response(some_serialaizer(some_model.objects.all(), many=True).data)


def get_data(amount, some_model, some_serialaizer, arg):
    
    instances = some_model.objects.all()
    match(amount):
        case "singular":
            for instance in instances:
                if instance.id == arg:
                    serialized_instance = some_serialaizer(instance).data
                    return Response(serialized_instance, status.HTTP_200_OK)
            else:
                return error_bad_status()
        
        case "plural":

            serialized_instance_list = some_serialaizer(instances, many=True).data
            return Response(serialized_instance_list, status.HTTP_200_OK)
        
        case _:
            return error_bad_status()


def delete_data(arg, some_model, some_serialaizer):

    try:
        old_model = some_model.objects.get(id=arg)
        old_model.delete()
        return Response(some_serialaizer(some_model.objects.all(), many=True).data)
    except:
        return error_bad_status()
    
    
def put_data(req, arg, some_model, some_serialaizer):
    old_model_object = some_model.objects.get(id=arg)
    
    try:
        update_item = some_serialaizer(old_model_object, data=req.data, partial = True)
        update_item.is_valid(raise_exception=True)
        update_item.save()
        return Response(some_serialaizer(some_model.objects.all(), many=True).data)
    except:
        return error_bad_status()
    
class Movies(ViewSet):
    def movies(self, req):
        return get_data('plural', Movie, SerializedMovie, '')
        
    def movie(self, req, arg):
        return get_data('singular', Movie, SerializedMovie, arg)

    def create_movie(self, req):
        return post_data(req, Movie, SerializedMovie)

    def delete_movie(self, req, arg):
        return delete_data(arg, Movie, SerializedMovie)

    def put_movie(self, req, arg):
        return put_data(req, arg, Movie, SerializedMovie)


class Tickets(APIView):
    def get(self, req, *args, **kwargs):
        a = req.META['PATH_INFO'].split('/')[-1]
        try:
            return get_data('singular', Ticket, SerializedTicket, int(a))
        except:
            return get_data('plural', Ticket, SerializedTicket, '')

    def post(self, req):
        if req.data['movie_id']:
            req.data['movie_id'] = Movie.objects.get(id=req.data['movie_id'])
            req.data['owner'] = User.objects.get(id=req.data['owner'])
        return post_data(req, Ticket, SerializedTicket)
    
    def delete(self, req, arg):
        return delete_data(arg, Ticket, SerializedTicket)
        
        
@api_view(['GET', 'POST'])
def users(req):
    if req.method == 'GET':
        return get_data('plural', User, UserSerializer, '')
    
    elif req.method == 'POST':
        return post_data(req, User, UserSerializer)
        
    else:
        return error_bad_status()


@api_view(['GET', 'PUT', 'DELETE'])
def user(req, arg):
    if req.method == 'GET':
        return get_data('singular', User, UserSerializer, arg)
        
    elif req.method == 'PUT':
        return put_data(req, arg, User, UserSerializer)
        
    elif req.method == 'DELETE':
        return delete_data(arg, User, UserSerializer)

    else:
        return error_bad_status()


class Places:
    @staticmethod
    @api_view(['GET', 'POST',])
    def places(req):     
        
        if req.method == 'GET':
            return get_data('plural', Place, SerializedPlace, '')
    
        elif req.method == 'POST':
            
            try:
                tickets = Ticket.objects.filter(id=req.data["ticket_id"])
                req.data['ticket_id'] = tickets[0]
            except:
                return error_bad_status()

            hold_places = list(Place.objects.filter(ticket_id=tickets[0].id))
            
            list_of_places = ('_,'*20).split(',')
            list_of_places.pop()
            print(list_of_places)
            for place in hold_places:
                if list_of_places[place.number-1] == '_' :
                    list_of_places[place.number-1] = place.number
                else:
                    return error_bad_status()
                    
            if list_of_places[(req.data["number"] - 1 )] == '_':
                list_of_places[(req.data["number"] - 1 )] = req.data["number"]

            
            for free_place in list_of_places:
                if free_place == '_' :
                    req.data["number"] = list_of_places.index(free_place) + 1
            
            print(list_of_places)
            return post_data(req, Place, SerializedPlace)
                    
                    
        else:
            return error_bad_status()
            
    @staticmethod
    @api_view(['GET', 'DELETE'])
    def place(req, arg):     
        if req.method == 'GET':
            return get_data('singular', Place, SerializedPlace, arg)

        elif req.method == 'DELETE':
            return delete_data(arg, Place, SerializedPlace)
        
        else:
            return error_bad_status()