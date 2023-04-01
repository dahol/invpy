from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000, blank=True)
    spec = models.CharField(max_length=200, blank=True)
    cpu = models.CharField(max_length=200, blank=True)
    mem = models.CharField(max_length=200, blank=True)
    disk0 = models.CharField(max_length=200, blank=True)
    disk1 = models.CharField(max_length=200, blank=True)
    disk2 = models.CharField(max_length=200, blank=True)
    disk3 = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Time', auto_now=True)
    # make = models.ForeignKey(Make, on_delete=models.CASCADE)
    # model = models.ForeignKey(Model, on_delete=models.CASCADE)
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Part(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000, blank=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Time', auto_now=True)
    # make = models.ForeignKey(Make, on_delete=models.CASCADE)
    # model = models.ForeignKey(Model, on_delete=models.CASCADE)
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000, blank=True)
    finished = models.BooleanField(null=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Time', auto_now=True)

    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000, blank=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Time', auto_now=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000, blank=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Time', auto_now=True)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000, blank=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True)
    updated_at = models.DateTimeField('Updated Time', auto_now=True)
    # make = models.ForeignKey(Make, on_delete=models.CASCADE)
    # model = models.ForeignKey(Model, on_delete=models.CASCADE)
    #task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
