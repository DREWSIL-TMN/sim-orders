from rest_framework import serializers
from orders.models import Order, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'number']


class OrderSerializer(serializers.ModelSerializer):
    manager = ClientSerializer()  # вложенный сериализатор
    adresse = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'manager', 'adresse', 'time_create', 'status']

    def get_adresse(self, obj):
        return {
            'location': obj.location,
            'caption': obj.caption,
        }
