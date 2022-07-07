from turtle import title
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import GenreModel, eBook
from .serializers import Genresserializer, eBookserializer, UserRegSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/book-list/',
        'Detail View': '/book-details/<int:pk>',
        'Create': '/genre-create/' + '/ebook-create/',
        'Update': '/book-update/<int:pk>',
        'Delete': '/book-delete/<int:pk>',
        'filter': '/get_books/' , # ?genre=Fantasy
        'Register':'/RegisterUser/',
        'login':'/login/',
    }
    return Response(api_urls)

# Create Genre of books


@api_view(['POST'])
def GenreCreate(request):
    serializer = Genresserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Create eBook


@api_view(['POST'])
def eBookCreate(request):
    serializer = eBookserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# List view of ebooks


@api_view(['GET'])
def BookList(request):
    qs = eBook.objects.all().order_by('-id')

    serializers = eBookserializer(qs, many=True)
    return Response(serializers.data)


# Detail View (each one)
@api_view(['GET'])
def Book_Details(request, pk):
    qs = eBook.objects.filter(id=pk)
    serializers = eBookserializer(qs, many=True)
    return Response(serializers.data)


# Update eBook
@api_view(['POST'])
def Book_Update(request, pk):
    qs = eBook.objects.filter(id=pk).first()
    serializer = eBookserializer(instance=qs, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete Book


@api_view(['DELETE'])
def Delete_Book(request, pk):
    qs = eBook.objects.filter(id=pk).first()
    qs.delete()
    return Response("Deleted successfully")

# filter


@api_view(['GET'])
def get_books(request):
    genre = request.query_params.get('genre', None)
    books = eBook.objects.all()
    if genre:
        qs = GenreModel.objects.filter(title=genre)
        for title in qs:
            books = books.filter(genre=title.id)
    if books:
        serialized = eBookserializer(books, many=True)
        return Response(serialized.data)


# Register
@api_view(['POST'])
def RegisterUser(request):
    serializer = UserRegSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'registered'
        data['username'] = account.username
        data['email'] = account.email
        token,create = Token.objects.get_or_create(user=account)
        data['token'] = token.key

    else:
        data = serializer.errors
    return Response(data)
 

 