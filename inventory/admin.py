from django.contrib import admin
from .models import Item, Task, Model, Make, Project, Part

# Register your models here.

admin.site.register(Project)
admin.site.register(Item)
admin.site.register(Task)
admin.site.register(Model)
admin.site.register(Make)
admin.site.register(Part)
