from rest_framework.permissions import IsAuthenticated
from .serializers import Taskserializers, Statusserializers
from todo.models import Task, Status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import CustomPagination

class TaskListViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = Taskserializers
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "author": ["exact","in"],
        "status": ["exact","in"],
  
    }
    search_fields = ['=title', 'description']
    ordering_fields = ['created_date']
    pagination_class = CustomPagination

class StatusListModuleSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = Statusserializers
    queryset = Status.objects.all()
    


'''class TaskListViewSet(viewsets.ViewSet):
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
    '''