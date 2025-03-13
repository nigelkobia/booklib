from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def create(self, request, *args, **kwargs):
    #     if len(request.data.get('isbn', '')) != 13:
    #         return Response({'error': 'ISBN must be 13 characters long.'}, status=status.HTTP_400_BAD_REQUEST)
    #     return super().create(request, *args, **kwargs)

    # @action(detail=False, methods=['get'])
    # def by_author(self, request):
    #     author = request.query_params.get('author', None)
    #     if author:
    #         books = Book.objects.filter(author=author)
    #         serializer = self.get_serializer(books, many=True)
    #         return Response(serializer.data)
    #     return Response({'error': 'Author parameter not provided'}, status=400)


