from django.conf import settings

import authaction.conditions


def get(action):

    return settings.AUTH_ACTION_CONDITIONS.get(
        action,
        authaction.conditions.forbidden,
    )
