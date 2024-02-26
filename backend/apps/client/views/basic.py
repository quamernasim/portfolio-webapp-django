from rest_framework.views import APIView
from ..serializers.basic import BasicInfoSerializer, SocialMediaSerializer, EducationSerializer
from ..serializers.auth import AuthUserSerializer
from ..models.basic import BasicInfo, SocialMedia, Education
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# ROOT_USER = 'quamer23nasim38@gmail.com'

# Create your views here.

class BasicInfoView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        basic = BasicInfo.objects.filter(user=request.user)
        if basic.exists():
            basic_first = basic.first()
            basic_serializer = BasicInfoSerializer(basic_first)
            user_serializer = AuthUserSerializer(basic_first.user)
            
            data = {'message': 'Data found',
                    'status': status.HTTP_200_OK,
                    'data': {
                        'basic': basic_serializer.data,
                        'user': user_serializer.data
                    }}
            return Response(data)
        else:
            data = {'message': 'No data found',
                    'status': status.HTTP_204_NO_CONTENT,
                    'data': {}}
            return Response(data)

    def post(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(user=request.user)
        if basic.exists():
            print(basic.first())
            data = {'message': 'Data already exists',
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': {}}
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
                print(serializer.errors)
                data = {'message': 'Bad Request',
                        'status': status.HTTP_400_BAD_REQUEST,
                        'data': serializer.errors}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(user=request.user)
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
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': {}}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(user=request.user)
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
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': {}}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, *args, **kwargs):
        basic = BasicInfo.objects.filter(user=request.user)
        if basic.exists():
            basic.delete()
            data = {'message': 'Data deleted',
                    'status': status.HTTP_200_OK,
                    'data': {}}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'message': 'No data found',
                    'status': status.HTTP_204_NO_CONTENT,
                    'data': {}}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
class SocialMediaView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        social = SocialMedia.objects.filter(user=request.user)
        if social.exists():
            social_first = social.first()
            social_serializer = SocialMediaSerializer(social_first)
            user_serializer = AuthUserSerializer(social_first.user)
            
            data = {'message': 'Data found',
                    'status': status.HTTP_200_OK,
                    'data': {
                        'social': social_serializer.data,
                        'user': user_serializer.data
                    }}
            return Response(data)
        else:
            data = {'message': 'No data found',
                    'status': status.HTTP_204_NO_CONTENT,
                    'data': {}}
            return Response(data)
    def post(self, request, *args, **kwargs):
        social = SocialMedia.objects.filter(user=request.user)
        if social.exists():
            data = {'message': 'Data already exists',
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': {}}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = SocialMediaSerializer(data=request.data)
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
        social = SocialMedia.objects.filter(user=request.user)
        if social.exists():
            serializer = SocialMediaSerializer(social.first(), data=request.data)
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
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': {}}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, *args, **kwargs):
        social = SocialMedia.objects.filter(user=request.user)
        if social.exists():
            serializer = SocialMediaSerializer(social.first(), data=request.data, partial=True)
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
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': {}}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        social = SocialMedia.objects.filter(user=request.user)
        if social.exists():
            social.delete()
            data = {'message': 'Data deleted',
                    'status': status.HTTP_200_OK,
                    'data': {}}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'message': 'No data found',
                    'status': status.HTTP_204_NO_CONTENT,
                    'data': {}}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
class EducationView(APIView):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request):
		education_objects = Education.objects.filter(user=request.user)
		if education_objects.exists():
			degree_query = request.data.get('degree')
			degree = education_objects.filter(degree__icontains=degree_query)
		
			if degree.exists():
				education_serializer = EducationSerializer(degree, many=True)
				data = {'message': 'Degree Exists',
						'status': status.HTTP_200_OK,
						'data': education_serializer.data}
				return Response(data)
			else:
				data = {'message': 'This Degree does not exists',
						'status': status.HTTP_204_NO_CONTENT,
						'data': {}}
			return Response(data)
		else:
			data = {'message': 'No Education data found',
					'status': status.HTTP_204_NO_CONTENT,
					'data': {}}
			return Response(data)
	def post(self, request, *args, **kwargs):
		education_objects = Education.objects.filter(user=request.user)
		if education_objects.exists():
			degree_query = request.data.get('degree')
			degree = education_objects.filter(degree__icontains=degree_query)
			if degree.exists():
				data = {'message': 'Data already exists for this degree',
						'status': status.HTTP_400_BAD_REQUEST,
						'data': {}}
				return Response(data, status=status.HTTP_400_BAD_REQUEST)
			else:
				serializer = EducationSerializer(data=request.data)
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
		else:
			serializer = EducationSerializer(data=request.data)
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