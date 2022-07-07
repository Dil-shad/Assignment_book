from rest_framework import serializers
from .models import GenreModel, eBook
from django.contrib.auth.models import User




class Genresserializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = "__all__"


class eBookserializer(serializers.ModelSerializer):
    genre_title = serializers.ReadOnlyField()

    class Meta:
        model = eBook
        fields = "__all__"



class UserRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password","password2"]

    def save(self):
        reg = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self._validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'passwod does not match'})
        reg.set_password(password)
        reg.save()
        return reg
