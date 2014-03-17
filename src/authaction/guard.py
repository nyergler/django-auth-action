import functools
import authaction.actions


def auth_action_required(action):

    def decorator(f):

        @functools.wraps(f)
        def _inner(*a, **kw):

            request = a[0]
            authaction.actions.get(action)(request.user, request.session)
            return f(*a, **kw)

        return _inner

    return decorator
