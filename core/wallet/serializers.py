# serializers.py
from rest_framework import serializers
from .models import EthModel, UsdModel

class EthSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthModel
        fields = ['user','amount']

class BtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsdModel
        fields = ['user','amount']

