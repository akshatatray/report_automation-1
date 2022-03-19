from django.contrib import admin
from .models import Project , Tag , Task , SubTask

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(SubTask)
# Register your models here.
