from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def home(request):
    

    if request.method == 'POST':
        
        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            form = TaskForm()

    else:
        form = TaskForm()

    status_filter = request.GET.get('status', 'incomplete')

    if status_filter == 'completed':
        tasks = Task.objects.filter(completed=True)
    else:
        tasks = Task.objects.filter(completed=False)

    

    return render(request, 'todo/home.html', {
        'form':form, 
        'tasks':tasks,
        'status_filter':status_filter, 
    })

def edit(request, id):
    if request.method == 'POST':
        pi = Task.objects.get(pk = id)
        fm = TaskForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = Task.objects.get(pk = id)
        fm = TaskForm(instance=pi)
    
    return render(request, 'todo/update.html', {'form':fm})

def delete(request, id):
    if request.method == 'POST':
        data = Task.objects.get(pk = id)
        data.delete()
        return HttpResponseRedirect('/')

def mark_complete(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def mark_incomplete(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = False
    task.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'todo/task_detail.html', {'task': task})

