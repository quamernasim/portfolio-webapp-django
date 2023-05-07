import requests as req
from django.conf import settings
import jwt
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

SECRECT_KEY = settings.SJWT_SECRET_KEY
ALGORITHM = settings.SJWT_ALGORITHM

API_ENDPOINT = settings.API_ENDPOINT
API_CLIENT_ENDPOINT = settings.API_CLIENT_ENDPOINT

def is_access_token_expired(token):
    try:
        decoded_token = jwt.decode(str(token), SECRECT_KEY, algorithms=ALGORITHM)
        return False, decoded_token
    except jwt.ExpiredSignatureError:
        return True, None

def refresh_token(request, reverse_url):
    refresh_token = request.COOKIES.get('refresh_token')

    headers = {'Authorization': 'Bearer ' + refresh_token}
    response = req.get(API_ENDPOINT + API_CLIENT_ENDPOINT + 'refresh_token/', headers=headers)

    response_json = response.json()
    new_access_token = response_json['access_token']
    response = redirect(reverse(reverse_url))
    response.set_cookie('access_token', new_access_token, httponly=True)
    return response