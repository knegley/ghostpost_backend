from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'date_created',
            'last_updated',
            'up_votes',
            'down_votes',
            'message',
            'message_type',
            'vote_total'
        ]
