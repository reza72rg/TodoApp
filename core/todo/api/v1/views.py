from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import Taskserializers
from todo.models import Task
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets




class TaskListViewSet(viewsets.ViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = Taskserializers
    queryset = Task.objects.all()
    
    def list(self, request):
        serializer = self.serializer_class(Task.objects.all(), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        task_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(task_object)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)

    def update(self, request, pk=None):
        task_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(task_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
  

    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        task_object = get_object_or_404(self.queryset, pk=pk)
        task_object.delete()
        return Response({'detail':"Item removed successfully"},status=status.HTTP_204_NO_CONTENT) 