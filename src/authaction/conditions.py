import authaction as authaction_constants
import authaction.exceptions


def logged_in(user, session):
    """User must be authenticated."""

    if user.is_authenticated():
        return True

    raise authaction.exceptions.ConditionFailed(
        action_hint=authaction_constants.LOGIN,
    )


def is_anonymous(user, session):
    """User is required to be anonymous."""

    if user.is_anonymous():
        return True

    raise authaction.exceptions.ConditionFailed(
        action_hint=authaction_constants.LOGOUT,
    )


def backend_required(backend):
    """Return authaction condition that requires the specified backend."""

    def condition(user, session):

        if getattr(user, 'backend', None) == backend:
            return True

        raise authaction.exceptions.ConditionFailed()

    return condition
