from django.urls import path
from . import views


# Creacion de nuestras propias urls a partir de lo puesto en views
urlpatterns = [
    path('', views.index, name="index"), # url principal
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('detail.html',   views.projects, name="projects"),
    # path('tasks/<str:title>', views.task),
    path('tasks/', views.task, name="tasks"),
    path('create_task/', views.create_task, name="create_tasks"),
    path('create_project/', views.create_project, name="create_project"),
]
