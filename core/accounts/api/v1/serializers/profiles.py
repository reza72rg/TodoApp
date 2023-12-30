from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email',read_only=True)
    class Meta:
        model = Profile
        fields = ['id','email','first_name','last_name','image','descriptions']
    
        
            