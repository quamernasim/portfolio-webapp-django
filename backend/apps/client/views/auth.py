from rest_framework.views import APIView
from ..serializers.auth import AuthUserSerializer
from rest_framework.response import Response
from ..models.auth import AuthUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse

import jwt
from django.conf import settings

SECRECT_KEY = settings.SJWT_SECRET_KEY
ALGORITHM = settings.SJWT_ALGORITHM

class Register(APIView):
    def post(self, request):
        serializer = AuthUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'success',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        }
        return response

class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = AuthUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        access_token  = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)
        
        response = Response()

        response.data = {
            'access_token': str(access_token),
            'refresh_token': str(refresh_token),
            'message': 'success',
            'status': status.HTTP_200_OK,
            'data': {}
        }

        return response

def refresh_token(request):    
    refresh_token = request.headers.get('Authorization').split(' ')[1]
    refresh_token_obj = RefreshToken(refresh_token)
    new_access_token = refresh_token_obj.access_token
    new_refresh_token = refresh_token_obj.get('refresh_token')
    response = Response()
    response.data = {'access_token': str(new_access_token)}
    return JsonResponse(response.data, status=200)

class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        token = request.headers.get('Authorization').split(' ')[1]

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = AuthUser.objects.filter(id=payload['id']).first()
        serializer = AuthUserSerializer(user)
        return Response(serializer.data)

    
