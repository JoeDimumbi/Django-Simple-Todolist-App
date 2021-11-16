from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def todolist(request):    
    if request.method == "POST":    #To post data in the database
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all() #To access/read data from the database
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks })

def index(request):
    context = {
        'index_text':"Welcome to Index Page"
    }
    return render(request, 'index.html', context)

def delete_task(request, task_id):      #To delete data from the database
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    messages.success(request,("Task Deleted!"))

    return redirect('todolist')

def edit_task(request, task_id):      #To edit data from the database
    if request.method == "POST":    #To post data in the database
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id) #To edit data from the database
        return render(request, 'edit.html', {'task_obj': task_obj })

def complete_task(request, task_id):      #To mark task as complete in the database
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def pending_task(request, task_id):      #To mark task as pending in the database
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')

def about(request):
    context = {
        'about_text':"Welcome to about us Page"
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'contact_text':"Welcome to contact us Page"
    }
    return render(request, 'contact.html', context)