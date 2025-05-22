from rest_framework import serializers

class DeepSeekInputSerializer(serializers.Serializer):
    source = serializers.CharField()
    data = serializers.CharField()