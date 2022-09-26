import jwt
from django.utils.timezone import datetime, timedelta

import auth_settings


def create_refresh_token(userID: int) -> str:
    refreshToken = jwt.encode(
        payload={
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=30),
        },
        key=auth_settings.SECRET_KEY,
        algorithm="HS256",
    )

    from refreshTokens import RefreshTokens
    RefreshTokens.objects.create(
        user_id=userID,
        refreshToken=refreshToken,
    )

    return refreshToken


def create_access_token(userID: int) -> str:
    return jwt.encode(
        payload={
            "userID": userID,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=1),
        },
        key=auth_settings.SECRET_KEY,
        algorithm="HS256",
    )
