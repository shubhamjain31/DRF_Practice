from rest_framework import serializers
from .models import Employee

# -------------------------------------------------- @Simple Serializers@ ------------------------------------------------
# class EmployeeSerializer(serializers.Serializer):
#     name            = serializers.CharField(max_length=30)
#     email           = serializers.EmailField()
#     password        = serializers.CharField(max_length=40)
#     phone           = serializers.CharField(max_length=40)

#     def create(self, validated_data):
#         obj = Employee.objects.create(**validated_data)
#         return obj

#     def update(self, instance, validated_data):
#         obj = Employee(**validated_data)
#         obj.id = instance.id
#         obj.save()
#         return obj

# -------------------------------------------------- @Model Serializers@ ------------------------------------------------
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        # fields = ['name']