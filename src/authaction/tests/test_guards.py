from unittest import TestCase

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.http import HttpRequest

from authaction.tests.factories import (
    UserFactory,
)
import authaction.conditions
import authaction.exceptions
import authaction.guard


class GuardTests(TestCase):

    def setUp(self):

        settings.AUTH_ACTION_CONDITIONS = {
            'testing': authaction.conditions.logged_in,
        }

    def test_auth_action_required_decorator(self):

        @authaction.guard.auth_action_required('testing')
        def test_psuedo_view(request):
            return "Called and returned."

        request = HttpRequest()

        # simulate auth and session middleware
        request.user = UserFactory.create()
        request.session = {}

        self.assertEqual(
            test_psuedo_view(request),
            'Called and returned.',
        )

    def test_auth_action_required_decorator_with_failure(self):

        @authaction.guard.auth_action_required('testing')
        def test_psuedo_view(request):
            return "Called and returned."

        request = HttpRequest()

        # simulate auth and session middleware
        request.user = auth_models.AnonymousUser()
        request.session = {}

        with self.assertRaises(authaction.exceptions.ConditionFailed):
            test_psuedo_view(request)
