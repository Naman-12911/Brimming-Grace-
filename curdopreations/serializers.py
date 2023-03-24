from rest_framework import serializers
from .models import Employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email','name','employe_id','date','phone']
