from django.db.models import fields
from rest_framework import serializers
from .models import Task
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task', 'description', 'created_date','due_date')


class TaskRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task', 'description', 'created_date','due_date')