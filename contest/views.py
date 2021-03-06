from .serializer import *
from contest.models import *
from rest_framework import viewsets


class ContestView(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer


class CollegeView(viewsets.ModelViewSet):
    queryset = Colleges.objects.all()
    serializer_class = CollegesSerializer


class ChallengeView(viewsets.ModelViewSet):
    queryset = Challenges.objects.all()
    serializer_class = ChallengeSerializer


class ViewView(viewsets.ModelViewSet):
    queryset = View_Stats.objects.all()
    serializer_class = ViewsStatsSerializer


class SubmitView(viewsets.ModelViewSet):
    queryset = Submission_Stats.objects.all()
    serializer_class = SubmitSerializer

