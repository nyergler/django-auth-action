from unittest import TestCase

from django.contrib.auth import models as auth_models

from authaction.tests.factories import (
    UserFactory,
)
import authaction as authaction_constants
import authaction.conditions
import authaction.exceptions


class BasicConditionTests(TestCase):

    def test_logged_in_passes_for_authd_user(self):

        self.assertTrue(
            authaction.conditions.logged_in(UserFactory.create(), {})
        )

    def test_logged_in_fails_for_anonymous_user(self):

        with self.assertRaises(authaction.exceptions.ConditionFailed) \
             as assertion:

            authaction.conditions.logged_in(auth_models.AnonymousUser(), {})

        self.assertEqual(
            assertion.exception.action_hint,
            authaction_constants.LOGIN,
        )

    def test_is_anonymous_passes_for_anonymous_user(self):

        self.assertTrue(
            authaction.conditions.is_anonymous(auth_models.AnonymousUser(), {})
        )

    def test_is_anonymous_fails_for_authed_user(self):

        with self.assertRaises(authaction.exceptions.ConditionFailed)\
             as assertion:

            authaction.conditions.is_anonymous(UserFactory.create(), {})

        self.assertEqual(
            assertion.exception.action_hint,
            authaction_constants.LOGOUT,
        )


class AuthBackendConditionTests(TestCase):

    def test_user_backend_required(self):

        condition = authaction.conditions.backend_required('testing')
        test_user = UserFactory.create()
        test_user.backend = 'testing'

        self.assertTrue(
            condition(test_user, {})
        )

    def test_user_backend_required(self):

        condition = authaction.conditions.backend_required('testing')
        test_user = UserFactory.create()
        test_user.backend = 'two-factor'

        with self.assertRaises(authaction.exceptions.ConditionFailed)\
             as assertion:

            condition(test_user, {})
