from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ToDoList, status_choices


# Create your views here.
def index(request):
    to_do_list = ToDoList.objects.all()
    return render(request, 'index.html', context={'to_do_list': to_do_list})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', context={"status_choices": status_choices})
    else:
        task = ToDoList.objects.create(
            description=request.POST.get("description"),
            status = request.POST.get("status"),
            full_description = request.POST.get("full_description"),
            deadline = request.POST.get("deadline"),
        )

        return redirect("task_detail", pk=task.pk)

def task_detail(request, *args, pk, **kwargs):
    task = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'task_detail.html', context={"task": task})