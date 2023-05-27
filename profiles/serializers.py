from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_staff = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    following_id = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Get the id of the following instance if the user is authenticated
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'username',
            'created_at',
            'updated_at',
            'name',
            'is_staff',
            'is_owner',
            'profile_image',
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
        ]
