from rest_framework.views import APIView
from ..forms.basic import BasicInfoForm, SocialMediaForm
from ..serializers.basic import BasicInfoSerializer, SocialMediaSerializer, EducationSerializer
from ..models.basic import BasicInfo
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status

ROOT_USER = 'quamer23nasim38@gmail.com'

# Create your views here.

class BasicInfoView(APIView):
    def get(self, request):
        basic = BasicInfo.objects.filter(email=ROOT_USER)
        if basic.exists():
            serializer = BasicInfoSerializer(basic.first())
            data = {'message': 'Data found',
                    'status': status.HTTP_200_OK,
                    'data': serializer.data}
            return Response(data, template_name='index.html')
        else:
            data = {'message': 'No data found',
                    'status': status.HTTP_204_NO_CONTENT}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    def post(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(email=ROOT_USER)
        if basic.exists():
            data = {'message': 'Data already exists',
                    'status': status.HTTP_400_BAD_REQUEST}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BasicInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {'message': 'Data created',
                        'status': status.HTTP_201_CREATED,
                        'data': serializer.data}
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {'message': 'Bad Request',
                        'status': status.HTTP_400_BAD_REQUEST,
                        'data': serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(email=ROOT_USER)
        if basic.exists():
            serializer = BasicInfoSerializer(basic.first(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {'message': 'Data updated',
                        'status': status.HTTP_200_OK,
                        'data': serializer.data}
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {'message': 'Data not updated',
                        'status': status.HTTP_400_BAD_REQUEST,
                        'data': serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {'message': 'Bad Request',
                    'status': status.HTTP_400_BAD_REQUEST}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(email=ROOT_USER)
        if basic.exists():
            serializer = BasicInfoSerializer(basic.first(), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {'message': 'Data updated',
                        'status': status.HTTP_200_OK,
                        'data': serializer.data}
                return Response(data, status=status.HTTP_200_OK)
            else:
                data = {'message': 'Data not updated',
                        'status': status.HTTP_400_BAD_REQUEST,
                        'data': serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = {'message': 'Bad Request',
                    'status': status.HTTP_400_BAD_REQUEST}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(email=ROOT_USER)
        if basic.exists():
            basic.delete()
            data = {'message': 'Data deleted',
                    'status': status.HTTP_200_OK}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'message': 'No data found',
                    'status': status.HTTP_204_NO_CONTENT}
            return Response(data, status=status.HTTP_204_NO_CONTENT)