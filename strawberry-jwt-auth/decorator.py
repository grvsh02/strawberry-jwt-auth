from functools import wraps


def login_required(resolver):
    @wraps(resolver)
    def wrapper(parent, info, *args, **kwargs):
        userID = getattr(info.context, "userID", None)
        if userID is not None:
            return resolver(parent, info, *args, **kwargs)
        return None
    return wrapper

