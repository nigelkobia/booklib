from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # override the default create, list, update, delete functions
    def create(self, request, *args, **kwargs):
            if len(request.data.get('isbn', '')) != 13:
                return Response({'error': 'ISBN must be 13 characters long.'}, status=status.HTTP_400_BAD_REQUEST)
            return super().create(request, *args, **kwargs)

    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    