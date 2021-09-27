from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        user = User.objects.create(
            validated_data['username'],
            first_name=validated_data['first_name'],  
            last_name=validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password'],
        )

        return user