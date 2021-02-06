from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def todo_list(request):
	context = dict()
	context['todo_list'] = Todo.objects.all(); 
	return render(request, 'todos/index.html', context)

def insert_todo(request):
	
	todo = Todo(content = request.POST['content'])
	todo.save()

	return redirect('/')

def delete_todo_item(request, todo_id):
	todo_to_delete = Todo.objects.get(id=todo_id)
	todo_to_delete.delete()
	
	return redirect('/')	
