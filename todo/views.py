from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def all_tasks(request):
    tasks = Todo.objects.all()
    return render(request, 'all_tasks.html', {'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        name = request.POST['name']
        if name is not None:
            task = Todo.objects.create(name=name)
            task.save()
            print('Task Saved')
        else:
            print('Whoops! Can not proceed -> Name is empty.')
    else:
        return render(request, 'add_task.html')
    return redirect('all_tasks')

def remove_task(request, id):
    task = Todo.objects.filter(id=id).exists()
    if task is not None:
        Todo.objects.get(id=id).delete()
        print('Task removed')
    return redirect('all_tasks')