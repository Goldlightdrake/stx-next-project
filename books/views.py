import django_filters.rest_framework
import requests
from django.shortcuts import render, redirect
from rest_framework import generics

from .filters import BookFilter
from .forms import BookForm
from .models import *
from .serializers import BookSerializer


def table(request):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs

    return render(request, 'books/table.html', {'books': books, 'book_filter': book_filter})


def create_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')

    context = {'form': form}
    return render(request, 'books/form.html', context)


def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    context = {'form': form}
    return render(request, 'books/form.html', context)


def delete_book(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('/books')

    return render(request, 'books/table.html')


def get_books_from_api(request):
    if 'search_terms' in request.GET and request.GET['search_terms'] != '':
        search_terms = '+'.join(request.GET['search_terms'].split(' '))
        url = f'https://www.googleapis.com/books/v1/volumes?q={search_terms}'
        response = requests.get(url)
        data = response.json()
        books = data['items']

        for book in books:
            book = book['volumeInfo']
            isbn_number = None
            for i in book['industryIdentifiers']:
                if i['type'] == "ISBN_13":
                    isbn_number = i['identifier']

            published_date = book['publishedDate'].split('-')
            if len(published_date) == 1:
                published_date.append('01')
                published_date.append('01')
            elif len(published_date) == 2:
                published_date.append('01')
            published_date = '-'.join(published_date)

            page_count = 0
            if "pageCount" in book:
                page_count = book['pageCount']
            try:
                book_data = Book(
                    title=book['title'],
                    author=book['authors'][0],
                    published_date=published_date,
                    ISBN_number=isbn_number,
                    page_count=page_count,
                    preview_link=book['previewLink'],
                    language=book['language']
                )
                book_data.save()
            except KeyError:
                print('something went wrong with API')

    return redirect('/books/')


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = "__all__"
