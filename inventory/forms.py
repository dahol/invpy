from django import forms
from django.utils.timezone import datetime
from django.utils import timezone
from .models import Item, Task, Model, Make, Project, Part


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description", max_length=10000)


class CreateNewTask(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description", max_length=10000)


class CreateNewPart(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description", max_length=10000)


class CreateNewMake(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description", max_length=10000)


class CreateNewModel(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description", max_length=10000)


class CreateNewItem(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description", max_length=10000)


class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # image = forms.ImageField(required=False)
        fields = ['name', 'desc', 'cpu', 'mem',
                  'disk0', 'disk1', 'disk2', 'disk3', 'disk4', 'image']


# class ItemForm(forms.ModelForm):
#    class Meta:
#        model = Item
#        fields = ['name', 'desc', 'image']  # plus any other fields you have

    # add this line if 'image' is not an ImageField in your model
    # image = forms.ImageField(required=False)
