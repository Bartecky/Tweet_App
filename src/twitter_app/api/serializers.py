from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from twitter_app.models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]