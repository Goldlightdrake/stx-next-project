from django.urls import path

from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('create-book/', views.create_book, name='create_book'),
    path('update-book/<str:pk>/', views.update_book, name='update_book'),
    path('delete-book/<str:pk>/', views.delete_book, name='delete_book'),
    path('get-books-from-api/', views.get_books_from_api, name='get_books_from_api'),
    path('api/v1/', views.BookListView.as_view(), name='books_list_view')
]
