from rest_framework import serializers
from .models import UserAccount, Notes,


# NotesSerializer serializer
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['title', 'slug', 'body', 'date_updated']