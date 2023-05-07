from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

#views.py
from django.shortcuts import render, redirect  
from todo_list.forms import TodoTaskForm  
from todo_list.models import TodoTask  
# Create your views here.  


def addnew(request):  
    if request.method == "POST":  
        form = TodoTaskForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = TodoTaskForm()  
    return render(request,'todo_list/index.html',{'form':form}) 

 
def index(request):  
    todolist = TodoTask.objects.order_by('duedate')
    return render(request,"todo_list/show.html",{'todolists':todolist}) 

 
def edit(request, id):  
    todolist = TodoTask.objects.get(id=id)  
    return render(request,'todo_list/edit.html', {'todolist':todolist}) 

 
def update(request, id):  
    todolist = TodoTask.objects.get(id=id)  
    form = TodoTaskForm(request.POST, instance = todolist)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'todo_list/edit.html', {'todolist': todolist})  


def destroy(request, id):  
    todolist = TodoTask.objects.get(id=id)  
    todolist.delete()  
    return redirect("/") 

def home(request):
    return render(request, 'todo_list/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'todo_list/register.html', context)