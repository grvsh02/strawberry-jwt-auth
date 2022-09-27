# strawberry-jwt-auth

A JWT auth library based on Django and strawberry.

## About
Auth is a flexible, drop-in solution to add authentication and authorization services to your applications. Your team and organization can avoid the cost, time, and risk that come with building your own solution to authenticate and authorize users.

## Features
- **JWT**: The library uses JSON Web Tokens to send information about an authenticated user. This information can be used to authorize access to resources without the need to query the database again.
- **Refresh Tokens**: The library also provides a refresh token to allow users to request a new access token without having to re-authenticate.
- **Blacklisting**: Refresh tokens can be blacklisted to prevent them from being used again. This is useful for logging out users or preventing them from accessing resources after a password change.
- **Token Revocation**: Refresh tokens can be revoked to prevent them from being used again. This is useful for logging out users or preventing them from accessing resources after a password change.
- **Token Verification**: The library provides a decorator to verify that a token is valid and has not been tampered with.
- **Fresh Login Requirement**: The library provides a decorator to verify that a user has logged in recently. This is useful for sensitive actions like changing a password or adding a new device to your account.
- **User Identity Lookup**: The library provides a method to look up a user's identity (userID) from the access token.
- **Cookie Storage**: The library stores the JWT in an HTTP-only cookie to prevent it from being accessed by JavaScript. This is useful for SPAs that use cookies for authentication.

## Installation
1. Install the package from PyPI:
```bash
pip install strawberry-jwt-auth
```

2. Add `strawberry_jwt_auth` to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    "strawberry_jwt_auth",
]
```

3. Migrate the database:
```bash
python manage.py migrate
```

4. Add `strawberry_jwt_auth.extensions.JWTAuthExtension` to your strawberry schema extensions:-
```python
from strawberry_jwt_auth.extension import JWTExtension

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions = [
        ...
        JWTExtension,
    ]
)
```

5. Wrap your Strawberry GraphQL view with `strawberry_jwt_auth.view.auth_enabled_view`:
```python
from strawberry_jwt_auth.views import strawberry_auth_view 

urlpatterns = [
  ...
  path('graphql/', strawberry_auth_view(GraphQLView.as_view(schema=schema))),
  ),
]
```

6. Add Attributes to your login mutation:
```python
    @strawberry.mutation
    def login(self, info, email: str, password: str) -> bool:
        
        # Your Authentication logic goes here
        
    setattr(info.context, "userID", user.id)
    setattr(info.context.request, "issueNewTokens", True)
    setattr(info.context.request, "clientID", user.id)
    return True
```

7. Add Attributes to your logout mutation:
```python
    @strawberry.mutation
    def logout(self, info) -> bool:
        
        # Your logout logic goes here
        
    setattr(info.context.request, "revokeTokens", True)
    return True
```

8. ( Optional ) Add login_required decorator to your mutations:
```python
    from strawberry_jwt_auth.decorator import login_required

    @strawberry.mutation
    @login_required
    def change_password(self, info, old_password: str, new_password: str) -> bool:
        
        # Your change password logic goes here
        
    return True
```

9. ( Optional ) Add Authentication backend to your settings.py:
```python
# Use this backend to authenticate users using their email and password
AUTHENTICATION_BACKENDS = [
    "strawberry_jwt_auth.backends.JWTAuthBackend",
]
```
## Working
 Read about Auth0 [here](https://auth0.com/docs)

## Working Examples

![preview](https://user-images.githubusercontent.com/50337734/192553206-7f05d9b6-3c3e-4975-80e8-885c670c1703.png)

## Future Plans
- [ ] Add support for customizing fields like cookies name, token expiry, etc.
- [ ] Add support for customizing the refresh token model.
- [ ] Add support for more decorators like `fresh_login_required` and `roles_required`.
- [ ] Add support for customizing the user identity lookup.

