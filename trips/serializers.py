from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        return data
    
    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        return self.Meta.model.objects.create_user(**data)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password1', 'password2', 'first_name', 'last_name')
        read_only_fields = ('id',)