from django.shortcuts import render
import requests as req

# Create your views here.
def basic_info(request):
    # datas = BasicInfoView().get(request)
    response_from_backend = req.delete('http://127.0.0.1:8000/api/client/profile_update/')
    print(response_from_backend.json())
    return render(request, 'client/index.html')