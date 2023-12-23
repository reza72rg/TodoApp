from django.urls import path
from .views import * 


app_name = 'api-v1'

urlpatterns = [
    path('task/',TaskListViewSet.as_view({'get':'list','post':'create'}), name ='task-list'),
    path('task/<int:pk>/',TaskListViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name ='task-detail'),
    
]