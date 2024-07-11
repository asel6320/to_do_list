from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ToDoList
from webapp.validate import task_validate

# Create your views here.
def index(request):
    to_do_list = ToDoList.objects.all()
    return render(request, 'index.html', context={'to_do_list': to_do_list})

def create_task(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, "create_task.html", {"form": form})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        full_description = request.POST.get("full_description")
        deadline = request.POST.get("deadline")

        task = ToDoList(
            description=description,
            status=status,
            full_description=full_description,
            deadline=deadline
        )

        errors = task_validate(task)
        if not errors:
            task.save()
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = ToDoList.objects.create(
                description=description,
                status=status,
                full_description=full_description,
                deadline=deadline
            )
            return redirect("task_detail", pk=task.pk)

        return render(
            request,
            "create_task.html",
            {"errors": errors, "task": task},
            {"form": form}
        )

def task_detail(request, *args, pk, **kwargs):
    task = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'task_detail.html', context={"task": task})

def update_task(request, *args, pk, **kwargs):
    if request.method == "GET":
        task = get_object_or_404(ToDoList, pk=pk)
        form = TaskForm(initial={
            "description": task.description,
            "status": task.status,
            "full_description": task.full_description,
            "deadline": task.deadline,
        })
        return render(
            request, "update_task.html",
            context={"form": form}
        )
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = get_object_or_404(ToDoList, pk=pk)
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.full_description = form.cleaned_data['full_description']
            task.deadline = form.cleaned_data['deadline']
            task.save()
            return redirect("task_detail", pk=task.pk)
        else:
            return render(
                request,
                "update_task.html",
                {"form": form}
            )

def delete_task(request, *args, pk, **kwargs):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == "GET":
        return render(request, "delete_task.html", context={"task": task})
    else:
        task.delete()
        return redirect("tasks")

def delete_tasks(request):
    if request.method == 'POST':
        form = TaskDeleteForm(request.POST)
        if form.is_valid():
            tasks_to_delete = form.cleaned_data['tasks']
            tasks_to_delete.delete()
            return redirect('tasks')  # Redirect to task list view
    else:
        form = TaskDeleteForm()

    return render(request, 'delete_tasks.html', {'form': form})