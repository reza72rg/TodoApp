from accounts.models import  Profile
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated    
from rest_framework import generics
from ..serializers import ProfileSerializers

class ProfileApiViews(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()


    def get_object(self):
        queryset = self.get_queryset()
        object = get_object_or_404(queryset,user=self.request.user)
        return object