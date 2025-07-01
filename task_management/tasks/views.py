from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from datetime import datetime

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'priority']

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        due_start = self.request.query_params.get('due_start')
        due_end = self.request.query_params.get('due_end')
        if due_start and due_end:
            queryset = queryset.filter(due_date__range=[due_start, due_end])
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        return Response({'status': 'marked as completed'})