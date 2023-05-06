from django.shortcuts import render, redirect, reverse
import requests as req
# from .forms import BasicInfoForm

API_ENDPOINT = "http://127.0.0.1:8000/"
API_CLIENT_ENDPOINT = "api/client/"

# Create your views here.
def basic_info(request):
    # datas = BasicInfoView().get(request)
    response_from_backend = req.get(API_ENDPOINT + API_CLIENT_ENDPOINT + 'profile_update/')
    if response_from_backend.status_code == 200:
        data = response_from_backend.json()
        if data['status'] == 200:
            basic = data['data']
            return render(request, 'client/basic_info.html', {'basic': basic})
        elif data['status'] == 204:
            return render(request, 'client/info_add.html', {'basic': {}})
    else:
        return render(request, 'client/basic_info.html', {'basic': {}})

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