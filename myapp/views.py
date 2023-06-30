from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    title = "Welcome to Django course"
    return render(request, 'index.html', {
        'title': title,
    })


def hello(request, username):
    """"""
    return HttpResponse("<h1>Hello %s </h1>" % username)


def about(request):
    """"""
    username = "Rodriguezalexp"
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    """  # se guardan datos dentro de la tabla en formato json
    return JsonResponse(projects, safe=False) # el segundo parametro lo pide django al renderizar 
    """
    projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def task(request):
    """ task = Task.objects.get(title=title)
    return HttpResponse('task: %s' % task.title) """
    tasks = list(Task.objects.all())
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('/tasks/')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return(redirect('/projects/'))


def project_detail(request):
    return render(request, 'project/detail.html')