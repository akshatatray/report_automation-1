from django.db import models
from User.models import User

class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=400)
    createdBy = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    targetDate = models.DateTimeField(editable=True)
    teamMembers = models.ManyToManyField(User , related_name="teammembers")
    stakeHolders = models.ManyToManyField(User , related_name= "stakeholder")
    owners = models.ManyToManyField(User , related_name="owners")
    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self):
        return self.title

class Task(models.Model):
    STATUS = (('st1' , 'st1') , ('st2' , 'st2') , ('st3' , 'st3') , ('st4' , 'st4'))
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=400)
    project = models.ForeignKey(Project , null= False , on_delete=models.SET(0))
    createdBy = models.ForeignKey(User , null = True , on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(editable=True)
    assignee = models.ForeignKey(User , null = True , on_delete=models.SET_NULL , related_name="assignee")
    watchers = models.ManyToManyField(User , related_name="watchers")
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=70 ,default=STATUS[0], choices = STATUS)
    tags = models.ManyToManyField(Tag , blank=True)
    def __str__(self):
        return self.name


class SubTask(models.Model):

    name = models.CharField(max_length=70)
    task = models.ForeignKey(Task , on_delete=models.CASCADE)
    def __str__(self):
        return self.name

