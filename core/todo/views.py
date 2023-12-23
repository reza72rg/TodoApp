from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from todo.forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Task,Status
from django.views import View

# Task List View
class Tasklist(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/list_task.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Task Create View
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title',"description","status"]
    success_url = reverse_lazy('todo:task_list')

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Status.objects.all()
        return context
# Task Delete View
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy("todo:task_list")


# Task Complete View
class TaskDone(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.status != 'completed':
            task.status = get_object_or_404(Status, name='Completed')
            task.save()
        return redirect('todo:task_list')

# Task Update View
class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name_suffix = "_update"
    model = Task
    fields = ['title',"description","status"]
    success_url = reverse_lazy("todo:task_list")

    
    def form_valid(self, form):
        return super(TaskUpdate,self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Status.objects.all()
        return context