from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterApiViews(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
            } 
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    