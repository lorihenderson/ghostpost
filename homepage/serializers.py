from rest_framework import serializers

from homepage.models import BoastRoast


class BoastRoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoastRoast
        fields = [
            "id",
            "choices",
            "user_input",
            "upvotes",
            "downvotes",
            "time_posted",
        ]