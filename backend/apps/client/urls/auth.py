from django.urls import path
from ..views import auth

urlpatterns = [
    path('register/', auth.Register.as_view(), name='register'),
    path('login/', auth.Login.as_view(), name='login'),
    path('user/', auth.UserView.as_view(), name='user'),
    path('refresh_token/', auth.refresh_token, name='refresh_token'),

]