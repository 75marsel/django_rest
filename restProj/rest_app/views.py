from django.shortcuts import render, get_object_or_404
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def project_view(request):
    
    if request.method == "GET":
        projects = Project.objects.all() # queryset
        serializer = ProjectSerializer(projects, many=True) # serialize the project

        # or use get_object_or_404(Project, pk=pk)

        for project in projects:
            print(f"Project: {project.card_title} UUID: {project.id}")

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def get_detail_view(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except project.DoesNotExist:
        return Response(status=404)
    
    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProjectSerializer(project, data=request.data) # update the current data with data
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)