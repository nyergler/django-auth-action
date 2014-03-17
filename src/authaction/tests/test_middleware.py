from unittest import TestCase

from django.conf import settings
from django.http import (
    HttpRequest,
    HttpResponseRedirect,
)

import authaction as authaction_constants
import authaction.exceptions
import authaction.middleware


class AuthActionMiddlewareTests(TestCase):

    def setUp(self):

        self.middleware = authaction.middleware.AuthActionMiddleware()

    def test_middleware_catches_conditionfailed_and_redirects(self):

        exception = authaction.exceptions.ConditionFailed(
            target='/test/target',
        )

        response = self.middleware.process_exception(HttpRequest(), exception)

        self.assertIsInstance(
            response,
            HttpResponseRedirect,
        )
        self.assertEqual(
            response['Location'],
            '/test/target',
        )

    def test_exception_with_login_hints_uses_settings(self):

        exception = authaction.exceptions.ConditionFailed(
            action_hint=authaction_constants.LOGIN,
        )

        response = self.middleware.process_exception(HttpRequest(), exception)

        self.assertIsInstance(
            response,
            HttpResponseRedirect,
        )
        self.assertEqual(
            response['Location'],
            settings.LOGIN_URL,
        )

    def test_exception_with_unknown_hint_raises_runtime_error(self):

        exception = authaction.exceptions.ConditionFailed(
            action_hint='bogus',
        )

        with self.assertRaises(RuntimeError):
            self.middleware.process_exception(HttpRequest(), exception)
