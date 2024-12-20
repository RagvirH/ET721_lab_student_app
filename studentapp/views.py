from django.shortcuts import render
from .models import TodoList
from .forms import TodoListForm

def index(request):
    # Fetch all todo tasks from the database
    todo_tasks = TodoList.objects.all()
    form = TodoListForm()  # Create an instance of the form
    context = {
        'todo_tasks': todo_tasks,
        'form': form,
    }
    return render(request, 'to_do_list/index.html', context)

def home(request):
    # Render the home page
    return render(request, 'to_do_list/home.html')