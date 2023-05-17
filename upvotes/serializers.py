from rest_framework import serializers
from django.db import IntegrityError
from upvotes.models import UpVote


class UpVoteSerializer(serializers.ModelSerializer):
    """
    UpVote serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = UpVote
        fields = ['id',
                  'owner',
                  'post_title',
                  'created_at',
                  'post'
                  ]

    def create(self, validated_data):
        """
        Create an upvote instance.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                'You have already upvoted this post.'
            )
