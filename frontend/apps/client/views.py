from django.shortcuts import render, redirect, reverse
import requests as req
from django.conf import settings
import jwt
from .utils import refresh_token, is_access_token_expired

SECRECT_KEY = settings.SJWT_SECRET_KEY
ALGORITHM = settings.SJWT_ALGORITHM

# from .forms import BasicInfoForm

API_ENDPOINT = settings.API_ENDPOINT
API_CLIENT_ENDPOINT = settings.API_CLIENT_ENDPOINT

# Create your views here.
def basic_info(request):
    access_token = request.COOKIES.get('access_token')
    
    if not access_token:
        return redirect(reverse('login'))
    
    expired, decoded_access_token = is_access_token_expired(access_token)
    
    if expired:
        print('Token Expired, Getting new token')
        return refresh_token(request, 'basic_info')

    headers = {'Authorization': 'Bearer ' + access_token}
    response_from_backend = req.get(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', headers=headers)

    name = decoded_access_token['user_id']
    
    if response_from_backend.status_code == 200:
        response_from_backend = response_from_backend.json()

        if response_from_backend['status'] == 200:
            data = response_from_backend['data']
            return render(request, 'client/basic_info.html', {'data': data})
        elif response_from_backend['status'] == 204:          
            return render(request, 'client/info_add.html', {'data': {}, 'name': name})
    else:
        return render(request, 'client/basic_info.html', {'data': {}, 'name': name})

def parse_basic(request, user_id):
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
    data = {"user": user_id,
            "firstname": firstname, 
            "lastname": lastname, 
            "country_code": country_code, 
            "phone_number": phone_number, 
            "city": city, 
            "state": state, 
            "country": country, 
            "zip_code": zip_code, 
            "address": address}
    return data

def info_add(request):
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect(reverse('login'))
    expired, decoded_access_token = is_access_token_expired(access_token)
    if expired:
        print('Token Expired, Getting new token')
        return refresh_token(request, 'basic_info')
    name = decoded_access_token['user_id']
    headers = {'Authorization': 'Bearer ' + access_token}
    data = parse_basic(request, name)
    response_from_backend = req.post(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', data = data, headers=headers)
    return redirect(reverse('basic_info'))

def info_update(request):
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect(reverse('login'))
    expired, decoded_access_token = is_access_token_expired(access_token)
    if expired:
        print('Token Expired, Getting new token')
        return refresh_token(request, 'info_update')
    headers = {'Authorization': 'Bearer ' + access_token}

    if request.method == 'GET':
        response_from_backend = req.get(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', headers=headers)
        data = response_from_backend.json().get('data')
        return render(request, 'client/update_basic.html', {'data': data})
    elif request.method == 'POST':
        name = decoded_access_token['user_id']
        data = parse_basic(request, name)
        response_from_backend = req.put(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', data = data, headers=headers)
        return redirect(reverse('basic_info'))
    
def delete_info(request):
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        return redirect(reverse('login'))
    expired, decoded_access_token = is_access_token_expired(access_token)
    if expired:
        print('Token Expired, Getting new token')
        return refresh_token(request, 'info_update')
    headers = {'Authorization': 'Bearer ' + access_token}

    req.delete(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/', headers=headers)
    return redirect(reverse('basic_info'))

def login(request):
    if request.method == 'GET':
        if 'access_token' in request.COOKIES:
            return redirect(reverse('basic_info'))
        return render(request, 'client/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {'email': email, 
                'password': password}
        response_from_backend = req.post(API_ENDPOINT + API_CLIENT_ENDPOINT + 'login/', data = data)
        if response_from_backend.status_code == 200:
            data = response_from_backend.json()
            if data['status'] == 200:
                access_token = data['access_token']
                refresh_token = data['refresh_token']
                response = redirect(reverse('basic_info'))
                response.set_cookie(key='access_token', value=access_token, httponly=True)
                response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
                return response
            else:
                print('check 1')
                return render(request, 'client/login.html', {'message': 'Invalid Credentials'})
        else:
            print('check 2')
            return render(request, 'client/login.html', {'message': 'Invalid Credentials'})
        
def register(request):
    if request.method == 'GET':
        if 'access_token' in request.COOKIES:
            return redirect(reverse('basic_info'))
        return render(request, 'client/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = {'name': name, 
                'email': email, 
                'password': password}
        
        response_from_backend = req.post(API_ENDPOINT + API_CLIENT_ENDPOINT + 'register/', data = data)

        if response_from_backend.status_code == 200:
            data = response_from_backend.json()
            if data['status'] == 201:
                return redirect(reverse('login'))
            else:
                return render(request, 'client/register.html', {'message': 'Invalid Input'})
        else:
            return render(request, 'client/register.html', {'message': 'Invalid Input'})
        
def logout(request):
    response = redirect(reverse('login'))
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

