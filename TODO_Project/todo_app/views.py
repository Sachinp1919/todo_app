from django.shortcuts import render, redirect
from .models import Todo_Task
from .forms import TodoTaskForm, TaskUpdateForm
from datetime import date


def add_task(request):
    template_name = 'todo_app/add.html'
    form = TodoTaskForm()
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.task_status = 'Pending'
            obj.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def show_task(request):
    template_name = 'todo_app/show.html'
    data = Todo_Task.objects.all()
    context = {'Todo_Task': data}
    return render(request, template_name, context)


def update_details(request, pk):
    template_name = 'todo_app/update.html'
    obj = Todo_Task.objects.get(pk=pk)
    form = TaskUpdateForm(instance=obj)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.task_status == 'Complated':
                obj.task_completed = date.today()
            obj.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def delete_details(request, pk):
    template_name = 'todo_app/conf.html'
    obj = Todo_Task.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'form': obj}
        return render(request, template_name, context)
    obj.delete()
    return redirect('show_url')