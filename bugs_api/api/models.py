from django.db import models


class Project(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True)
    name = models.CharField(max_length=50)


class User(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True)
    username = models.CharField(max_length=50)


class Bug(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
