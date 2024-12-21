from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('id')
    context = {'tasks': tasks}
    return render(request, 'to_do_list/index.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'to_do_list/add_task.html', {'form': form})

def delete_all_completed(request):
    Task.objects.filter(completed=True).delete()
    return redirect('index')

def delete_all(request):
    Task.objects.all().delete()
    return redirect('index')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')