import django_filters

from .models import *


class BookFilter(django_filters.FilterSet):
    published_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ("title", "author", "language", "published_date")
