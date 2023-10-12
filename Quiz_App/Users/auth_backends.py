from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserAuthBackend(ModelBackend):
    def authenticate(self, request, name=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(name=name)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
