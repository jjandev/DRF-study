from rest_framework import serializers
from .models import Movie, Actor, Review


# Model Serializer 사용
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date']


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
        # extra_kwargs = {
        #     'movie': {'read_only': True},
        # }

class MovieSerializer(serializers.ModelSerializer):
    # reviews = serializers.StringRelatedField(many=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'name', 'reviews', 'opening_date', 'running_time', 'overview']
        # read_only_fields = ['review_set']

# Serializer 사용
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     opening_date = serializers.DateField()
#     running_time = serializers.IntegerField()
#     overview = serializers.CharField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.opening_date = validated_data.get('opening_date', instance.opening_date)
#         instance.running_time = validated_data.get('running_time', instance.running_time)
#         instance.overview = validated_data.get('overview', instance.overview)
#         instance.save()
#         return instance


# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     gender = serializers.CharField
#     birth_date = serializers.DateField()

#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.birth_date = validated_data.get('birth_date', instance.birth_date)
#         instance.save()
#         return instance