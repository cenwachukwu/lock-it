from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes, UserAccount
from .serializers import NotesSerializer, RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "successfully registered new user"
            data["email"] = account.email
            data["username"] = account.username
        else:
            data = serializer.errors
        return Response(data)


# The root of our API is going to be a view that supports listing all the existing notes.
@api_view(['GET',])
def notes_list(request):

    """
    List all code notes, or create a new note.
    """
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)


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
def notes_delete_view(request, slug):

    """
    delete a note.
    """

    try:
        notes = Notes.objects.get(slug=slug)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = notes.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


# post/create notes
@api_view(['POST',])
def notes_create_view(request):

    """
    create a note.
    """
    account = UserAccount.objects.get(pk=1)
    # pk = primary key

    # now we have to get the user b/c without the user, you cant make a new note
    notes = Notes(user=account)
    if request.method == "POST":
        # here we pass a the note that already has a user to the serializer
        serializer = NotesSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(data = data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


