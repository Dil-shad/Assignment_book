
from django.test import TestCase
import requests
from requests.auth import HTTPBasicAuth
# Create your tests here.

response = requests.get("http://127.0.0.1:8000/api/book-list")
# print(type(response))
# print(response.json())

res = requests.get("http://127.0.0.1:8000/api/book-details/1")
# print(res.url)


# filter by genre
p = {'genre': 'Thriller'}


def filter_val(arg):
    filter_resp = requests.get("http://127.0.0.1:8000/api/get_books", params=p)
    return filter_resp.json()

# print(filter_val(p))


# create user
payload = {"username": "user_new", "email": "rq611606@gmail.com",
           "password": "user_new", "password2": "user_new"}


def create_user(arg):
    post_resp = requests.post("http://127.0.0.1:8000/api/RegisterUser", data=payload)
    return post_resp.json()

# print(create_user(payload))


# update_books
update_payload = {
    "title": "API testing",
    "author": "API TTT",
    "review": 5,
    "favorite": True,
    "genre": 3
}


def update_book(id, payload):
    update_resp = requests.put(f"http://127.0.0.1:8000/api/book-update/{id}", data=payload)
    print(update_resp.json())

# update_book(17,update_payload)


# delete

def delete_book(arg):
    del_resp = requests.delete(f"http://127.0.0.1:8000/api/book-delete/{arg}")
    print(del_resp.status_code)
    return del_resp.json()

# print(delete_book(18))


# auth_user
log = {
    'username': 'test_user',
    'password': 'test123'
}


def user_auth(log):
    log_res = requests.post('http://127.0.0.1:8000/api/login/', data=log)
    #print(log_res.status_code)
    r = log_res.json()
    return r


tok = user_auth(log)
print(tok)


# authorization
def authorization_request(arg):
    res = requests.get('http://127.0.0.1:8000/api/welcome',headers={'Authorization': f'token {arg}'})

    return res.json()


print(authorization_request(tok['token']))
