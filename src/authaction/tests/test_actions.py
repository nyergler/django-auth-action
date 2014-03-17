from unittest import TestCase

from django.conf import settings

import authaction.actions
import authaction.conditions
import authaction.exceptions


class ActionLookupTests(TestCase):

    def setUp(self):

        settings.AUTH_ACTION_CONDITIONS = {
            'test_condition': authaction.conditions.logged_in,
        }

    def test_lookup_returns_condition(self):

        self.assertEqual(
            authaction.actions.get('test_condition'),
            authaction.conditions.logged_in,
        )

    def test_unknown_lookup_fails_closed(self):

        condition = authaction.actions.get('add_to_cart')

        with self.assertRaises(authaction.exceptions.ConditionFailed):
            condition(None, {})
