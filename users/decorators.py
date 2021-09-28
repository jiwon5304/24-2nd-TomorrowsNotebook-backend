import jwt

from django.conf import settings
from django.http import JsonResponse

from my_settings import ALGORITHM
from .models import User

def login_decorator(func):
    def wraper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            if not access_token:
                request.user = None
                return func(self, request, *args, **kwargs)
            token = jwt.decode(access_token, settings.SECRET_KEY, algorithms = ALGORITHM)
            user = User.objects.get(id = token['id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE': 'ENCODE_ERROR'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)
        return func(self, request, *args, **kwargs)
    return wraper