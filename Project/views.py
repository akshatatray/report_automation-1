from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProjectSerializer, TagSerializer, TaskSerializer, SubTaskSerializer
from .models import Project, Tag, Task, SubTask


# ALL PROJECT VIEWS
class ProjectView(APIView):
    def get(self, request):
        project = Project.objects.all()
        response = ProjectSerializer(project, many=True)
        return Response({"data": response.data}, status=200)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


# PROJECT BY ID
class SpecificProjectView(APIView):
    def get(self, req, id):
        project = Project.objects.get(id=id)
        res = ProjectSerializer(project)
        return Response({"Data": res.data}, status=200)
