from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        print("EmailBackend.authenticate")
        UserModel = get_user_model()
        try:
            if email is not None:
                user = UserModel.objects.get(email=email)
            else:
                user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            pass
        return None
