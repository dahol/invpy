from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("item/<int:id>", views.item, name="item"),
    path("item/all", views.items, name="items"),

    path("task/all", views.tasks, name="tasks"),
    path("task/<int:id>", views.task, name="task"),

    path("make/<int:id>", views.make, name="make"),
    path("make/all", views.makes, name="makes"),

    path("part/<int:id>", views.part, name="part"),
    path("part/all", views.parts, name="parts"),

    path("model/<int:id>", views.model, name="model"),
    path("model/all", views.models, name="models"),

    path("project/<int:id>", views.project, name="project"),
    path("project/all", views.projects, name="projects"),

    path("create_project", views.create_project, name="create_project"),
    path("create_task", views.create_task, name="create_task"),
    path("create_part", views.create_part, name="create_part"),
    path("create_make", views.create_make, name="create_make"),
    path("create_model", views.create_model, name="create_model"),
]
