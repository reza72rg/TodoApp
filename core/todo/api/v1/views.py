from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import requests
from django.http import JsonResponse
from django.views import View
from .serializers import Taskserializers, Statusserializers, Usersserializers
from .pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from accounts.models import User
from todo.models import Task, Status


class TaskListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = Taskserializers
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "author": ["exact", "in"],
        "status": ["exact", "in"],
    }
    search_fields = ["=title", "description"]
    ordering_fields = ["created_date"]
    pagination_class = CustomPagination

    @method_decorator(cache_page(60 * 5))  # Cache for 5 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class StatusListModuleSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Statusserializers
    queryset = Status.objects.all()


class UsersListModuleSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Usersserializers
    queryset = User.objects.all()


class WeatherApi(View):
    def get(self, request, *args, **kwargs):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": "Tehran",  # Replace with the desired city name
            "appid": "23db3c61c5a56bdcb6c098685539fdf8",
        }
        response = requests.get(url, params=params)
        data = response.json()

        return JsonResponse(
            data
        )  # Convert data to JsonResponse and return it

    @method_decorator(cache_page(60 * 20))  # Cache for 5 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


"""class TaskListViewSet(viewsets.ViewSet):
    #permission_classes =[IsAuthenticated]
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
        return Response({'detail': "Item removed successfully"},
        status=status.HTTP_204_NO_CONTENT)
"""
