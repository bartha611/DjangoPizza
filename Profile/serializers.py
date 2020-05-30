from .models import Profile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=Profile.objects.all())])
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Profile.objects.all())])

    class Meta:
        model = Profile
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Profile(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
