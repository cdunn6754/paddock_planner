from rest_framework import serializers


class TeamupEventSerializer(serializers.Serializer):
    title = serializers.CharField()
    start = serializers.TimeField()
    end = serializers.TimeField()
