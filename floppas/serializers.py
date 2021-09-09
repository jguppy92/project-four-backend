from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Chat, Message
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'image')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class PopulatedMessageSerializer(MessageSerializer):
    sender = NestedUserSerializer()

class ChatSerializer(serializers.ModelSerializer):
    messages_in_chat = PopulatedMessageSerializer(many=True, read_only=True)
    user_one_id = NestedUserSerializer()
    user_two = NestedUserSerializer()

    class Meta:
        model: Chat
        fields = '__all__'