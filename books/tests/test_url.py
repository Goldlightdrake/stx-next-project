from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import *


class TestUrls(SimpleTestCase):
    def test_table_url_is_resolved(self):
        url = reverse('table')
        self.assertEquals(resolve(url).func, table)

    def test_create_book_url_is_resolved(self):
        url = reverse('create_book')
        self.assertEquals(resolve(url).func, create_book)

    def test_update_book_url_is_resolved(self):
        url = reverse('update_book', args=[1, ])
        self.assertEquals(resolve(url).func, update_book)

    def test_delete_book_url_is_resolved(self):
        url = reverse('delete_book', args=[1, ])
        self.assertEquals(resolve(url).func, delete_book)

    def test_books_list_view_url_is_resolved(self):
        url = reverse('books_list_view')
        self.assertEquals(resolve(url).func.view_class, BookListView)
