from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList  # Changed from ToDoList to TodoList
from .forms import TodoListForm  # Changed from form to forms
from django.views.decorators.http import require_POST

def index(request):
    todo_tasks = TodoList.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_tasks': todo_tasks, 'form': form}
    return render(request, 'to_do_list/index.html', context)  # Updated template path

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('text')
        if task_text:
            TodoList.objects.create(text=task_text)
        return redirect('index')

def delete_all_completed(request):
    TodoList.objects.filter(completed=True).delete()
    return redirect('index')

def complete_task(request, task_id):
    task = get_object_or_404(TodoList, id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(TodoList, id=task_id)
    task.delete()
    return redirect('index')

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = TodoList(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedTodo(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')
