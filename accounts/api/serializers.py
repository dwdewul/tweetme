from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    # follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            # 'follower_count',
        ]
    # def get_follow_count(self, obj):
    #     return 0
