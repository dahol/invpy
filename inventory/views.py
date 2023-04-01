from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Task, Model, Make, Project, Part
from .forms import CreateNewProject, CreateNewTask, CreateNewPart, CreateNewItem, CreateNewMake, CreateNewModel

# Create your views here.


def home(response):
    makes = Make.objects.all()[:5]
    models = Model.objects.all()[:5]
    parts = Part.objects.all()[:5]
    tasks = Task.objects.all()[:5]
    items = Item.objects.all()[:5]
    projects = Project.objects.all()[:5]
    return render(response, "inventory/home.html", {"makes": makes, "models": models, "parts": parts, "projects": projects, "tasks": tasks, "items": items})

# // TODO: Make some sort of dashboard on landing page

# Item


def item(response, id):
    i = Item.objects.get(id=id)
    return render(response, "inventory/item.html", {"item": i})


def items(response):
    items = Item.objects.all()
    return render(response, "inventory/items.html", {"items": items})


def create_item(response):
    if response.method == "POST":
        f = CreateNewItem(response.POST)
        if f.is_valid():
            n = f.cleaned_data["name"]
            d = f.cleaned_data["desc"]
            t = Item(name=n, desc=d)
            t.save()
        return HttpResponseRedirect("item/%i" % t.id)
    else:
        f = CreateNewItem()
    return render(response, "inventory/create_item.html", {"form": f})


# Make


def make(response, id):
    m = Make.objects.get(id=id)
    return render(response, "inventory/make.html", {"make": m})


def makes(response):
    makes = Make.objects.all()
    return render(response, "inventory/makes.html", {"makes": makes})


def create_make(response):
    if response.method == "POST":
        f = CreateNewMake(response.POST)
        if f.is_valid():
            n = f.cleaned_data["name"]
            d = f.cleaned_data["desc"]
            t = Make(name=n, desc=d)
            t.save()
        return HttpResponseRedirect("make/%i" % t.id)
    else:
        f = CreateNewMake()
    return render(response, "inventory/create_make.html", {"form": f})


# Model

def model(response, id):
    m = Model.objects.get(id=id)
    return render(response, "inventory/model.html", {"model": m})


def models(response):
    models = Model.objects.all()
    return render(response, "inventory/models.html", {"models": models})


def create_model(response):
    if response.method == "POST":
        f = CreateNewModel(response.POST)
        if f.is_valid():
            n = f.cleaned_data["name"]
            d = f.cleaned_data["desc"]
            t = Model(name=n, desc=d)
            t.save()
        return HttpResponseRedirect("model/%i" % t.id)
    else:
        f = CreateNewModel()
    return render(response, "inventory/create_model.html", {"form": f})


# Part


def part(response, id):
    p = Part.objects.get(id=id)
    return render(response, "inventory/part.html", {"part": p})


def parts(response):
    parts = Part.objects.all()
    return render(response, "inventory/parts.html", {"parts": parts})


def create_part(response):
    if response.method == "POST":
        f = CreateNewPart(response.POST)
        if f.is_valid():
            n = f.cleaned_data["name"]
            d = f.cleaned_data["desc"]
            t = Part(name=n, desc=d)
            t.save()
        return HttpResponseRedirect("part/%i" % t.id)
    else:
        f = CreateNewPart()
    return render(response, "inventory/create_part.html", {"form": f})


# Task

def task(response, id):
    t = Task.objects.get(id=id)
    return render(response, "inventory/task.html", {"task": t})


def tasks(response):
    tasks = Task.objects.all()
    return render(response, "inventory/tasks.html", {"tasks": tasks})


def create_task(response):
    if response.method == "POST":
        f = CreateNewTask(response.POST)
        if f.is_valid():
            n = f.cleaned_data["name"]
            d = f.cleaned_data["desc"]
            t = Task(name=n, desc=d)
            t.save()
        return HttpResponseRedirect("task/%i" % t.id)
    else:
        f = CreateNewTask()
    return render(response, "inventory/create_task.html", {"form": f})


# Project

def project(response, id):
    p = Project.objects.get(id=id)
    return render(response, "inventory/project.html", {"project": p})


def projects(response):
    projects = Project.objects.all()
    return render(response, "inventory/projects.html", {"projects": projects})


def create_project(response):
    if response.method == "POST":
        f = CreateNewProject(response.POST)
        if f.is_valid():
            n = f.cleaned_data["name"]
            d = f.cleaned_data["desc"]
            t = Project(name=n, desc=d)
            t.save()
        return HttpResponseRedirect("project/%i" % t.id)
    else:
        f = CreateNewProject()
    return render(response, "inventory/create_project.html", {"form": f})
