import os
import pickle
import base64
from datetime import datetime

from ..models import StolenItem, PictureStolen, PersonWithThing, PicturePerson
from django.contrib.auth.models import User

from .serializers import (StolenSerializer,
                          PictureStolenSerializer,
                          PersonSerializer,
                          PicturePersonSerializer,
                          UserSerializer,
                          )

from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class StolenAPI(generics.ListCreateAPIView):

    queryset = StolenItem.objects.all()
    serializer_class = StolenSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DetailStolenAPI(generics.RetrieveUpdateDestroyAPIView):

    model = StolenItem
    queryset = StolenItem.objects.all()
    serializer_class = StolenSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PictureStolenAPI(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):

    queryset = PictureStolen.objects.all()
    serializer_class = PictureStolenSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PersonAPI(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = PersonWithThing.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DetailPersonAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = PersonWithThing.objects.all()
    serializer_class = PersonSerializer


class PicturePersonAPI(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):

    queryset = PicturePerson.objects.all()
    serializer_class = PicturePersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # print(f'This is POST {request}, {len(request.data)}')
        # data = base64.b64decode(request.data.get('image'))
        # with open('image/person/img_from_post'+ str(datetime.now())+'.jpg', 'wb') as f:
        #     f.write(data)
        #
        # request.data._mutable = True
        # request.data['image'] = 'ok'
        # request.data._mutable = False
        return self.create(request, *args, **kwargs)


class UserAPI(APIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(username=kwargs.get('user'))
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class SearchAPI(APIView):

    def get(self, request, *args, **kwargs):
        search = StolenItem.objects.filter(vin=kwargs.get('search'))
        serializer = StolenSerializer(search,  many=True)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)