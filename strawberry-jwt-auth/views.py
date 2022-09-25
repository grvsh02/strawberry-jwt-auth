from functools import wraps

from jwt_generator import create_access_token, create_refresh_token


def strawberry_auth_view(get_response):
    def add_cookies_response(request, response):
        if hasattr(request, "issueNewTokens") and request.issueNewTokens:
            response.set_cookie(
                key="JWT_ACCESS_TOKEN",
                value=create_access_token(request.clientID)
            )
            response.set_cookie(
                key="JWT_REFRESH_TOKEN",
                value=create_refresh_token(request.clientID)
            )
        if hasattr(request, "revokeTokens") and request.revokeTokens:
            response.delete_cookie("JWT_ACCESS_TOKEN")
            response.delete_cookie("JWT_REFRESH_TOKEN")
        return response

    @wraps(get_response)
    def wrapper(request, *args, **kwargs):
        request.jwt_cookie = True
        response = get_response(request, *args, **kwargs)
        return add_cookies_response(request, response)

    return wrapper
