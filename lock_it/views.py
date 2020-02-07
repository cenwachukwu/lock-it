from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes, UserAccount
from .serializers import NotesSerializer

# Create your views here.
# get notes detail view
@api_view(['GET',])
def notes_detail_view(request, slug):
    try:
        notes = Notes.objects.get(slug=slug)
    except Notes.DoesNotExist:
        # use response when returning responses from the rest framework
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "Get"
        # here we are passing in a notes object into the NotesSerializer and returning the serialized data 
        serializer = NotesSerializer(notes)
        return Response(serializer.data)