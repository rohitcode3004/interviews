from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List': '/task-list',
		'Detail View': '/task-detail/<str:pk>/',
		'Create': '/task-create/',
		'Update': '/task-update/<str:pk>/',
		'Delete': '/task-delete/<str:pk>/',
	}

	return Response(api_urls)


@api_view(['GET'])
def studentList(request):
	students = Student.objects.all()
	serializer  = StudentSerializer(students, many=True)  #can return multiple objects
	return Response(serializer.data)


@api_view(['GET'])
def studentDetail(request, pk):
	student = Student.objects.get(id=pk)
	serializer  = StudentSerializer(student, many=False)  #can return one object only
	return Response(serializer.data)


@api_view(['POST'])
def studentCreate(request):
	serializer  = StudentSerializer(data=request.data)  #get data in json format

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def studentUpdate(request, pk):
	student = Student.objects.get(id=pk)
	serializer  = StudentSerializer(instance=student, data=request.data)  #get data in json format

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def studentDelete(request, pk):
	student = Student.objects.get(id=pk)
	student.delete()

	return Response("Item successfully deleted!")