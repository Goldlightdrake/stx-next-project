from django.test import TestCase, Client
from django.urls import reverse
from books.models import Book
import json


class TestViews(TestCase):
    def setUp(self):
        Book.objects.create(
            title='Mock Title',
            author='Mock Author',
            published_date='2022-01-01',
            ISBN_number=1234567890123,
            page_count=123,
            preview_link='https://www.books.pl',
            language='PL'
        )
        self.client = Client()
        self.mock_book_data = {'title': 'Mock Title', 'author': 'Mock Author', 'published_date': '01/01/2022',
                               'ISBN_number': 1234567890123, 'page_count': 123,
                               'preview_link': 'https://www.books.pl', 'language': 'PL'}

    def test_table_view(self):
        response = self.client.get(reverse('table'))
        self.assertTemplateUsed(response, 'books/table.html')
        self.assertEquals(response.status_code, 200)

    def test_create_book_view_post(self):
        response = self.client.post(reverse('create_book'),
                                    self.mock_book_data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/books/')

    def test_create_book_view_get(self):
        response = self.client.get(reverse('create_book'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/form.html')

    def test_update_book_view_post(self):
        response = self.client.post(reverse('update_book', args=[1, ]),
                                    self.mock_book_data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/books/')

    def test_update_book_view_get(self):
        response = self.client.get(reverse('update_book', args=[1, ]),
                                   self.mock_book_data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/form.html')

    def test_delete_book_view(self):
        response = self.client.post(reverse('update_book', args=[1, ]),
                                    self.mock_book_data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/books/')

    def test_get_books_from_api_view_empty_search_terms(self):
        response = self.client.get(reverse('get_books_from_api'))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/books/')

    def test_BookListView_view_class_without_query(self):
        response = self.client.get(reverse('books_list_view'))
        self.assertEquals(response.status_code, 200)
        response = json.loads(json.dumps(response.data))
        self.assertEqual(response[0]['title'], self.mock_book_data['title'])
