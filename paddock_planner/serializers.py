from rest_framework import serializers


class TeamupEventSerializer(serializers.Serializer):
    title = serializers.CharField()
    start_dt = serializers.DateTimeField()
    end_dt = serializers.DateTimeField()