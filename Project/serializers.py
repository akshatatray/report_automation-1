from rest_framework import serializers
from .models import Project, Tag, Task, SubTask


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', '.createdBy', 'createdAt', 'updatedAt', 'targetDate', 'teamMembers',
                  'stakeHolders', 'owners']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'project', 'createdBy', 'createdAt', 'updatedAt', 'assignee', 'watchers',
                  'type', 'status', 'tags']


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['name', 'task', 'status']
