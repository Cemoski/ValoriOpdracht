""""" 

In this file the functions/methods are defined. It tells the API what to do with the CRUD calls and gives 
responses and status call. It also renders the urls of the rest framework.  

"""""
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Intern
from .serializers import InternSerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/intern-list/',
		'Detail View':'/detail-intern/<str:pk>/',
		'Create':'/create-intern/',
		'Update':'/update-intern/<str:pk>/',
		'Delete':'/delete-intern/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def internList(request):
	if request.method == 'GET':
		intern = Intern.objects.all().order_by('id')
		serializer = InternSerializer(intern, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		return Response({})

@api_view(['GET'])
def detailIntern(request, pk):
	try:
		intern = Intern.objects.get(id=pk)
		serializer = InternSerializer(intern, many=False)
	except Intern.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	return Response(serializer.data)

@api_view(['POST'])
def createIntern(request):

	serializer = InternSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateIntern(request, pk):
	try:
		intern = Intern.objects.get(id=pk)
		serializer = InternSerializer(instance=intern, data=request.data, status=status.HTTP_200_OK)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
	except Intern.DoesNotExist:
		return Response('No such intern', status=status.HTTP_400_BAD_REQUEST, )

@api_view(['DELETE'])
def deleteIntern(request, pk):
	try:
		intern = Intern.objects.get(id=pk)
		intern.delete()
		return Response('Intern succesfully deleted out of the DB of Valori!')
	except Intern.DoesNotExist:
		return Response(status=status.HTTP_204_NO_CONTENT)
