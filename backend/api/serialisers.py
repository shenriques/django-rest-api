from rest_framework import serializers

class UserPublicSerialiser(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
