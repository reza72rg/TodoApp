from rest_framework import serializers
from todo.models import Task, Status
from accounts.models import Profile, User
       
class Taskserializers(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(many=False,slug_field='name',queryset= Status.objects.all())
    class Meta:
        model = Task
        fields = ["id","author","title","description","status","created_date"]
        read_only_fields = ["author"]
        
    
  
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)