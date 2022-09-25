from django.conf import settings

SECRET_KEY = (
    settings.JWT_ACCESS_TOKEN_KEY
    if hasattr(settings, "JWT_ACCESS_TOKEN_KEY")
    else settings.SECRET_KEY
)
