from django import forms
from django.utils.timezone import datetime
from django.utils import timezone


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
