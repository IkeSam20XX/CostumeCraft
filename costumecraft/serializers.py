#going from an object to a json
from rest_framework import serializers
from .models import Supply

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['id', 'name', 'material', 'amount', 'source', 'location', 'use']