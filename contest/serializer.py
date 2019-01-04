from rest_framework import serializers
from contest.models import *


class SubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission_Stats
        fields = '__all__'


class ViewsStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = View_Stats
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):

    view = ViewsStatsSerializer(many=True,read_only=True)
    submit = SubmitSerializer (many=True, read_only=True)

    class Meta:
        model = Challenges
        fields = '__all__'


class CollegesSerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer(many=True,read_only=True)

    class Meta:
        model = Colleges
        fields = '__all__'


class ContestSerializer(serializers.ModelSerializer):
    college = CollegesSerializer(many=True,read_only=True)

    class Meta:
        model = Contest
        fields = '__all__'




