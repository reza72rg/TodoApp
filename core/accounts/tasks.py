from celery import shared_task
from todo.models import Task, Status


@shared_task
def Delete_task_complete():
    state = Status.objects.get(name="Completed")
    response = Task.objects.filter(status=state)
    response.delete()
