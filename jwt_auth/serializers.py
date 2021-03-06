from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from floppas.serializers import ChatSerializer, LikedUserSerilizer, MessageIdSerializer

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})

        try:
            validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password': err.messages})

        data['password'] = make_password(password)

        return data

    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    # sent_messages = MessageIdSerializer(many=True)
    liked_users = LikedUserSerilizer(many=True)
    liked_by = LikedUserSerilizer(many=True)
    active_chats = ChatSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

class UserChatSerializer(serializers.ModelSerializer):
    sent_messages = MessageIdSerializer(many=True)
    liked_users = LikedUserSerilizer(many=True)
    liked_by = LikedUserSerilizer(many=True)
    active_chats = ChatSerializer(many=True)
