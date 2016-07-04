from rest_framework import serializers
from functions.models import Function, FunctionVersion


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function


class FunctionVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionVersion
