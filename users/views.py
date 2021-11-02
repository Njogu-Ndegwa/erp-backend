from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
import jwt
from django.conf import settings
from django.utils.encoding import smart_bytes, smart_str,\
    DjangoUnicodeDecodeError
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework import status, generics, permissions, exceptions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from .auth import generate_access_token, generate_refresh_token
from .serializers import UserSerializer, UserLoginSerializer
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import User
from datetime import datetime, timezone, timedelta


@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def create_new_account(request):
    """Have an ICT Admin able to create new account."""
    if request.method == 'GET':
        request_object = User.objects.all()
        serializer = UserSerializer(request_object, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['is_active'] = True
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def user_login_view(request):
    """Get user's email address and password"""
    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    if (email is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    """Validate both email and password
       check if user is active
    """
    try:
        user = User.objects.filter(email=email).first()
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('wrong credentials')

        if user.is_active is False:
            response.data = {
                "message": "You account is inactive. please follow the account reactivation process"
            }
            return response
        serialized_user = UserLoginSerializer(user).data

        """"Generate access token"""
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refreshtoken',
                            value=refresh_token, httponly=True)
            
        
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }
        
        user.save()
        return response
    except AttributeError:
        raise exceptions.AuthenticationFailed("No user exists with such email")
