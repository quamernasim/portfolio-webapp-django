from rest_framework.views import APIView
from ..serializers.auth import AuthUserSerializer
from rest_framework.response import Response
from ..models.auth import AuthUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import jwt, datetime
from django.conf import settings

secret_key = settings.SJWT_SECRET_KEY
algorithm = settings.SJWT_ALGORITHM

class Register(APIView):
    def post(self, request):
        serializer = AuthUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

from rest_framework_simplejwt.backends import TokenBackend

class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = AuthUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        token = AccessToken.for_user(user)
        
        response = Response()

        response.data = {
            'jwt': str(token),
            'message': 'success',
            'status': status.HTTP_200_OK,
            'data': {}
        }

        return response
    
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

    
