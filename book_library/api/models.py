from django.db import models

#In this BookViewSet, we define a queryset that returns all the Book instances, and we specify that the API should use the BookSerializer for data serialization.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
