from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import ToDoList, status_choices


# Create your views here.
def index(request):
    to_do_list = ToDoList.objects.all()
    return render(request, 'index.html', context={'to_do_list': to_do_list})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', context={"status_choices": status_choices})
    else:
        ToDoList.objects.create(
            description=request.POST.get("description"),
            status = request.POST.get("status"),
            deadline = request.POST.get("deadline"),
        )

        return HttpResponseRedirect('/')

def task_detail(request):
    pass