from django.shortcuts import render, get_object_or_404, redirect

from . import models
from .models import Task



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})



def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})



def task_create(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')


        task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date if due_date else None,
            due_time=due_time if due_time else None
        )
        return redirect('task_list')

    return render(request, 'task_form.html')



def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # Met à jour la tâche avec les nouvelles données
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.due_time = request.POST.get('due_time')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')

    return render(request, 'task_form.html', {'task': task})



def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return redirect('task_list')



def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':

        task.completed = not task.completed
        task.save()
        return redirect('task_list')

    return redirect('task_list')
