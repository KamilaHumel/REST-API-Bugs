from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import generics

from .models import Bug
from .permissions import IsBugOwner
from .serializers import BugSerializer


class BugList(generics.ListAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user_id", "project_id"]


class CreateBug(generics.CreateAPIView):
    serializer_class = BugSerializer
    permission_classes = [IsAuthenticated]


class UpdateBug(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BugSerializer
    queryset = Bug.objects.all()
    permission_classes = [IsBugOwner]
