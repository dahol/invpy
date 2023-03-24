from django import forms
from django.utils.timezone import datetime
from django.utils import timezone


class CreateNewProject(forms.Form):
    d = datetime.now()
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description")
    created_at = d
    updated_at = d


class CreateNewTask(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description")
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()


class CreateNewPart(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description")
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()


class CreateNewMake(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description")
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()


class CreateNewModel(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description")
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()


class CreateNewItem(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    desc = forms.CharField(label="Description")
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
