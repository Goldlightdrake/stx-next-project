from django.core.exceptions import ValidationError
from django.test import TestCase
from books.models import Book


class TestModels(TestCase):
    def test_book_creation_with_valid_data(self):
        valid_book = Book.objects.create(
            title='Mock Title',
            author='Mock Author',
            published_date='2022-01-01',
            ISBN_number=1234567890123,
            page_count=123,
            preview_link='https://www.books.pl',
            language='PL'
        )
        self.assertEquals(type(valid_book), Book)

    def test_book_creation_without_ISBN(self):
        valid_book = Book.objects.create(
            title='Mock Title',
            author='Mock Author',
            published_date='2022-01-01',
            page_count=123,
            preview_link='https://www.books.pl',
            language='PL'
        )
        self.assertEquals(type(valid_book), Book)

    def test_book_creation_with_invalid_date_format(self):
        self.assertRaises(
            ValidationError,
            lambda: Book.objects.create(
                title='Mock Title',
                author='Mock Author',
                published_date='12/12/2022',
                ISBN_number=1234567890123,
                page_count=123,
                preview_link='https://www.books.pl',
                language='PL'
            ))
