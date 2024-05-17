from django.shortcuts import redirect, render, get_object_or_404
from task.models import Catagory,Task
from task.models import Task
from task.forms import AddTaskForm
from django.contrib.auth import logout
from .forms import LoginForm,SignUpForm
# Create your views here.

def index(request):
    
    tasks_with_high = Task.objects.filter(priority='High')
    tasks_with_meduim = Task.objects.filter(priority='Medium')
    tasks_with_low = Task.objects.filter(priority='Low')
    catagory = Catagory.objects.all()
    
    context = {
        'tasks':tasks_with_high,
        'tasks_M':tasks_with_meduim,
        'tasks_L':tasks_with_low,
        'catagory':catagory
    }
    
    return render(request,'core/index.html',context)

def details(request,pk):
    
    task = Task.objects.get(pk=pk)
    print('view function is running')
    return render(request,'core/details.html',{'task':task})


def sign_up(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignUpForm()
    return render(request,'core/signup.html',{'form':form})


def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('core:index')




def edit_task(request,pk):
    task_got = get_object_or_404(Task,pk=pk)
    # task = AddTaskForm(instance=task_got)
    
    if request.method == 'POST':
        form = AddTaskForm(request.POST,instance=task_got)
        print('will save soon')
        if form.is_valid():
            form.save()
            print('task edited succesfully')
            return redirect('index')
    else:
        form = AddTaskForm(instance=task_got)
        print('edit form')
    
    return render(request,'core/task_edit.html',{'form':form})
         


def add_task(request):
    
    if request.method == 'POST':
        print('add task')
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
        
    form = AddTaskForm()
    print('new form')
    return render(request,'core/add_task.html',{'form':form})


def log_out(request):
    logout(request)
    
    return redirect('core:index')

    