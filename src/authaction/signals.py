from datetime import datetime

from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
)


def handle_user_logged_in(sender, user, request, **kwargs):
    """Set the last auth time in the session."""

    import authaction as authaction_constants

    request.session[authaction_constants.SESSION_LAST_AUTH] = datetime.now()


def handle_user_logged_out(sender, user, request, **kwargs):
    """Clear the last auth time from the session."""

    import authaction as authaction_constants

    if authaction_constants.SESSION_LAST_AUTH in request.session:
        del request.session[authaction_constants.SESSION_LAST_AUTH]


user_logged_in.connect(handle_user_logged_in)
user_logged_out.connect(handle_user_logged_out)
