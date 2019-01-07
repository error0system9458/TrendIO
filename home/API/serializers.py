from rest_framework import serializers
from home.models import Post



class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = (
            'pk',
            'post',
            'user',
            'image_post',
            'created',
            'updated',
        )

        read_only_field = ['user','created','updated']
