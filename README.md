# Assignment_book

# steps for run this project

virtual env
#after activating virtual env 
-"python manage.py makemigration",
-"python manage.py migrate",
-"python manage.py runserver"


-superuser:admin
    pasword:admin
    
   api_urls = {
        'list': '/book-list/',
        'Detail View': '/book-details/<int:pk>',
        'Create': '/genre-create/' + '/ebook-create/',
        'Update': '/book-update/<int:pk>',
        'Delete': '/book-delete/<int:pk>',
        'filter by genre,i.e ?genre=Fantasy': '/get_books/',
        'Register':'/RegisterUser/',
        'login':'/login/',
        'Authorization':'/welcome/',
    }
    
- you can test API using tests.py file or Postman.
exiting User=
    'username': 'test_user',
    'password': 'test123'


- **Thanks For Reading **


