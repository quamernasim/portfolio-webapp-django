from django.shortcuts import render, redirect, reverse
import requests as req
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
import jwt

secret_key = settings.SJWT_SECRET_KEY
algorithm = settings.SJWT_ALGORITHM

# from .forms import BasicInfoForm

API_ENDPOINT = "http://127.0.0.1:8000/"
API_CLIENT_ENDPOINT = "api/client/"

from rest_framework_simplejwt.backends import TokenBackend

# Create your views here.
def basic_info(request):
    jwt_token = request.COOKIES.get('jwt')
    if jwt_token:
        headers = {'Authorization': 'Bearer ' + jwt_token}
        response_from_backend = req.get(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', headers=headers)

        payload = jwt.decode(str(jwt_token), secret_key, algorithms=algorithm)
        name = payload['user_id']
        if response_from_backend.status_code == 200:
            data = response_from_backend.json()
            if data['status'] == 200:
                basic = data['data']
                return render(request, 'client/basic_info.html', {'basic': basic, 'name': name})
            elif data['status'] == 204:
                return render(request, 'client/info_add.html', {'basic': {}, 'name': name})
        else:
            return render(request, 'client/basic_info.html', {'basic': {}, 'name': name})
    else:
        return redirect(reverse('login'))

def parse_basic(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    country_code = request.POST.get('country_code')
    phone_number = request.POST.get('phone_number')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    zip_code = request.POST.get('zip_code')
    address = request.POST.get('address')
    data = {"firstname": firstname, 
            "lastname": lastname, 
            "email": email, 
            "country_code": country_code, 
            "phone_number": phone_number, 
            "city": city, 
            "state": state, 
            "country": country, 
            "zip_code": zip_code, 
            "address": address}
    return data

def info_add(request):
    data = parse_basic(request)
    response_from_backend = req.post(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', data = data)
    return redirect(reverse('basic_info'))

def info_update(request):
    if request.method == 'GET':
        response_from_backend = req.get(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/')
        data = response_from_backend.json().get('data')
        return render(request, 'client/update_basic.html', data)
    elif request.method == 'POST':
        data = parse_basic(request)
        response_from_backend = req.put(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', data = data)
        return redirect(reverse('basic_info'))
    
def delete_info(request):
    req.delete(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/')
    return redirect(reverse('basic_info'))

def login(request):
    if request.method == 'GET':
        if 'jwt' in request.COOKIES:
            return redirect(reverse('basic_info'))
        return render(request, 'client/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {'email': email, 'password': password}
        response_from_backend = req.post(API_ENDPOINT + API_CLIENT_ENDPOINT + 'login/', data = data)
        if response_from_backend.status_code == 200:
            data = response_from_backend.json()
            if data['status'] == 200:
                jwt_token = data['jwt']
                response = redirect(reverse('basic_info'))
                response.set_cookie(key='jwt', value=jwt_token, httponly=True)
                return response
            else:
                return render(request, 'client/login.html', {'message': 'Invalid Credentials'})
        else:
            return render(request, 'client/login.html', {'message': 'Invalid Credentials'})
        
def logout(request):
    response = redirect(reverse('login'))
    response.delete_cookie('jwt')
    return response