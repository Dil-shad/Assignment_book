from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('genre-create', views.GenreCreate, name='genre-create'),
    path('ebook-create', views.eBookCreate, name='ebook-create'),
    path('book-list', views.BookList, name='book-list'),
    path('book-details/<int:pk>', views.Book_Details, name='book-details'),
    path('book-update/<int:pk>', views.Book_Update, name='book-update'),
    path('book-delete/<int:pk>', views.Delete_Book, name='Book-delete'),
    path('get_books', views.get_books, name='get_books'),#filter
    #--------------------------------------------------------------------#
    path('RegisterUser',views.RegisterUser,name='RegisterUser'),
    path('login/',obtain_auth_token,name='login'),
    path('welcome',views.Welcome,name='welcome'),




]
