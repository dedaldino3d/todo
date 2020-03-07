from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from tasks.forms import TaskForm

from .models import Task
from django.contrib import messages


# Create your views here.
def helloworld(request):
    return HttpResponse("Hello World!You understand how it works!")


@login_required()
def tasklist(request):
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    else:

        task_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(task_list, 2)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, "tasks/tasklist.html", {'tasks': tasks})


@login_required()
def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) #pega o formulario que salva no BD e armazena na variavel

        if form.is_valid():
            task = form.save(commit=False) #para de salvar os dados no BD
            task.done = 'doing' #seta o atributo como doing
            task.user = request.user #envia apenas pro usuario autentiado
            task.save() #salva os dados no BD
            return redirect("/") #redireciona o usuario para a pagina principal
    else:
        form = TaskForm()
        return render(request, "tasks/addtask.html", {'form': form}) #retorna o request com o template e os argumentos necessarios


@login_required()
def editTask(request, id):
    task = get_object_or_404(Task, pk=id) #pega a task ou 404 caso contrario
    form = TaskForm(instance=task) #pega a instancia do BD Task e manda para o formulario

    if (request.method == 'POST'): #se o o request do formulario for o metodo POST, salva os dados na instancia do BD Task
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid):
            task = form.save()
            task.save()
            return redirect('/')
        else:
            return render(request, "tasks/editTask.html", {'form': form, 'task': task})
    else:
        return render(request, "tasks/editTask.html", {'form': form, 'task': task})


@login_required()
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, "Tarefa deletada com sucesso.")

    return redirect('/')


@login_required()
def tarefas(request):
    tarefas = Task.objects.all().order_by('-created_at').filter(user=request.user)

    return render(request, "tasks/tarefas.html", {'tarefas': tarefas})


@login_required()
def description(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, "tasks/description.html", {'task': task})


def yourname(request, name):
    return render(request, "tasks/yourname.html", {'name': name})
