from urllib import response
from django.test import TestCase
import requests
# Create your tests here.

response = requests.get("http://127.0.0.1:8000/api/book-list")
# print(type(response))
#print(response.json())


res = requests.get("http://127.0.0.1:8000/api/book-details/1")
# print(res.url)


p = {'genre': 'Thriller'}

filter_resp = requests.get("http://127.0.0.1:8000/api/get_books", params=p)
# print(filter_resp.json())


payload = {"username": "user_req", "email": "req611606@gmail.com",
           "password": "user123", "password2": "user123"}


#Create User
post_resp = requests.post("http://127.0.0.1:8000/api/RegisterUser", data=payload)
#print(post_resp.json() )



update_payload={
        "title": "API testing",
        "author": "API",
        "review": 5,
        "favorite": True,
        "genre": 3
    }
update_resp=requests.put("http://127.0.0.1:8000/api/book-update/6",data=update_payload)
print(update_resp.json())