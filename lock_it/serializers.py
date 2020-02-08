from rest_framework import serializers
from .models import UserAccount, Notes


# NotesSerializer serializer
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['title', 'slug', 'body', 'date_updated']

# RegistrationSerializer serializer
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserAccount
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    # before we save the userAccount, we have to validate the data and also make sure the two password matches
    def save(self):
        account = UserAccount(
            email=self.validated_data['email'],
            username=self.validated_data['username'],    
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],

        if password != password2:
            raise serializers.ValidationError({'password' : 'passwords must match.'})

        account.set_password(password)
        account.save()
        return account