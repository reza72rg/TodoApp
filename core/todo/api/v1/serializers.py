from rest_framework import serializers
from todo.models import Task, Status

       
class Taskserializers(serializers.ModelSerializer):
    
    status = serializers.SlugRelatedField(many=False,slug_field='name',queryset= Status.objects.all())
    class Meta:
        model = Task
        fields = ["id","user","title","description","status","created_date"]
        