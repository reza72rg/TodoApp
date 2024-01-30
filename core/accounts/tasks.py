from celery import shared_task
from todo.models import Task
import time
@shared_task
def Send_email():
    time.sleep(5)
    print("Done Sending hi reza")
    
    
@shared_task
def Delete_task_complete():
    response = Task.objects.filter(status = 3)
    response.delete()