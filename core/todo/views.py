from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Task, Status
import time
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60 * 30), name="dispatch")
class Tasklist(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/list_task.html"

    def get_queryset(self):
        time.sleep(10)
        return self.model.objects.filter(author=self.request.user.id)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "status"]
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(TaskCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Status.objects.all()
        return context


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task_list")


class TaskDone(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.status != "completed":
            task.status = get_object_or_404(Status, name="Completed")
            task.save()
        return redirect("todo:task_list")


class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name_suffix = "_update"
    model = Task
    fields = ["title", "description", "status"]
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        return super(TaskUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Status.objects.all()
        return context
