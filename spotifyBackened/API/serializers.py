from rest_framework import serializers
from .models import Room


class Roomserializers(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id', 'room_code', 'host_name', 'guest_can_stop', 'votes_to_change')

    

