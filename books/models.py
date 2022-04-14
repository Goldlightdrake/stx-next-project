from django.core.validators import RegexValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(help_text='Date format: Month/Day/Year')
    ISBN_number = models.CharField(null=True, max_length=13, validators=[
        RegexValidator(
            regex=r'^(\d{13})?$',
            message='ISBN number must contain only numbers and have 13 digits!',
        ),
    ])
    page_count = models.IntegerField()
    preview_link = models.URLField(max_length=200)
    language = models.CharField(max_length=2)

    def __str__(self):
        return self.title
