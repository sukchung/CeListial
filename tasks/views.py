from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/list.html", context)


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=task)
    context = {
        "form": form,
        "task": task,
    }
    return render(request, "tasks/edit.html", context)


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("show_my_tasks")

    context = {
        "task": task,
    }
    return render(request, "tasks/delete.html", context)
