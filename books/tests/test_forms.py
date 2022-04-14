from django.test import SimpleTestCase
from books.forms import BookForm


class TestForm(SimpleTestCase):
    def test_book_form_valid_data(self):
        form = BookForm({'title': 'Mock Title', 'author': 'Mock Author', 'published_date': '01/01/2022',
                         'ISBN_number': 1234567890123, 'page_count': 123,
                         'preview_link': 'https://www.books.pl', 'language': 'PL'})
        self.assertTrue(form.is_valid())

    def test_book_form_invalid_data(self):
        form = BookForm({'title': 'Mock Title', 'author': 'Mock Author', 'published_date': '01/01/2022',
                         'ISBN_number': 1234567, 'page_count': 123,
                         'preview_link': 'https://www.books.pl', 'language': 'PL'})
        self.assertFalse(form.is_valid())
