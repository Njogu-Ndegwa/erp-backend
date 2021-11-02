import datetime
import jwt
from django.conf import settings

def generate_access_token(user):
    """Generates access token to a specific employee"""
    access_token_payload = {
        'user_id': str(user.id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=3),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256')

    """Return refresh token"""
    return access_token


def generate_refresh_token(user):
    """Generates refresh token to a specific employee"""
    refresh_token_payload = {
        'user_id': str(user.id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')

    """Return refresh token"""
    return refresh_token