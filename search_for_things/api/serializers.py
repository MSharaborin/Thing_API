from django.contrib.auth.models import User

from ..models import StolenItem, PictureStolen, PersonWithThing, PicturePerson
from rest_framework import serializers
from drf_base64.serializers import ModelSerializer


class PictureStolenSerializer(ModelSerializer):

    class Meta:
        model = PictureStolen
        fields = '__all__'


class StolenSerializer(serializers.ModelSerializer):
    stolen = PictureStolenSerializer(many=True, read_only=True)

    class Meta:
        model = StolenItem
        fields = '__all__'


class PicturePersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PicturePerson
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    person = PicturePersonSerializer(many=True, read_only=True)

    class Meta:
        model = PersonWithThing
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active',)

