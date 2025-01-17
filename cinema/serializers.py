from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cinema.models import Movie


class CinemaSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
