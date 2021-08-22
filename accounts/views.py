from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100, min_length=8)

    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        # filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
        if User.objects.filter(email=email).exists():
            # if your username is existing get the query of your specific username
            user = User.objects.get(email=email)
            # then set the new password for your username
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error': f'User with email {email} not found'})


class ResetPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        data['username'] = slugify(data['email'])
        serializer = ResetPasswordSerializer(data=data)
        alldatas = {}
        if serializer.is_valid(raise_exception=True):
            mname = serializer.save()
            alldatas['data'] = 'Successful password reset.'
            return Response(alldatas, status=201)
        return Response('Failed to reset password', status=404)
