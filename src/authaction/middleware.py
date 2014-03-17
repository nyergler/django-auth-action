from django.conf import settings
from django.http import HttpResponseRedirect

import authaction as authaction_constants
import authaction.exceptions


class AuthActionMiddleware(object):

    def process_exception(self, request, exception):

        if isinstance(exception,
                      authaction.exceptions.ConditionFailed):

            if exception.target:
                target = exception.target

            elif exception.action_hint == authaction_constants.LOGIN:
                target = settings.LOGIN_URL

            elif exception.action_hint == authaction_constants.LOGOUT:
                target = settings.LOGOUT_URL

            else:
                raise RuntimeError("Unknown action_hint, no target specified.")

            return HttpResponseRedirect(target)
