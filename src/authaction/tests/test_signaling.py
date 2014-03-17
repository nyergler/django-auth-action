from unittest import TestCase

from django.http import HttpRequest
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)

import authaction as authaction_constants
from authaction.tests.factories import (
    UserFactory,
)


class UserSignalTests(TestCase):

    def test_login_signal_sets_authed_time(self):
        user = UserFactory()
        request = HttpRequest()
        request.session = {}

        user_logged_in.send(sender=user.__class__, request=request, user=user)

        self.assertIn(authaction_constants.SESSION_LAST_AUTH, request.session)

    def test_logout_signal_cleared_authed_time(self):

        user = UserFactory()
        request = HttpRequest()
        request.session = {
            authaction_constants.SESSION_LAST_AUTH: True,
        }

        user_logged_out.send(sender=user.__class__, request=request, user=user)

        self.assertNotIn(authaction_constants.SESSION_LAST_AUTH, request.session)
