from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    is_staff = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
            "is_staff",
            "is_owner",
            "profile_image",
            "following_id",
            "posts_count",
            "followers_count",
            "following_count",
        ]
