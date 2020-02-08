from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes, UserAccount
from .serializers import NotesSerializer

# The root of our API is going to be a view that supports listing all the existing notes, or creating a new note.
@api_view(['GET', 'POST'])
def notes_list(request):

    """
    List all code notes, or create a new note.
    """
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# get notes detail view
@api_view(['GET',])
def notes_detail_view(request, slug):

    """
    Retrieve a note.
    """

    try:
        notes = Notes.objects.get(slug=slug)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotesSerializer(notes)
        return Response(serializer.data)

# update notes with put request
@api_view(['PUT',])
def notes_update_view(request, slug):

    """
    update a note.
    """

    try:
        notes = Notes.objects.get(slug=slug)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NotesSerializer(notes, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            # so if it's successful we'll return ["success":"update successful"]
            data["success"] = "update successful"
            return Response(data = data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete notes
@api_view(['DELETE',])
def notes_update_view(request, slug):

    """
    update a note.
    """

    try:
        notes = Notes.objects.get(slug=slug)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NotesSerializer(notes, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            # so if it's successful we'll return ["success":"update successful"]
            data["success"] = "update successful"
            return Response(data = data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)