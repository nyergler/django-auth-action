import glob
import os
import sys

from django.conf import settings
try:
    settings.configure()
except RuntimeError:
    pass


def setup():
    """Perform test runner setup.

    This is its own function so we can easily call it from doctest
    ``testsetup`` blocks.

    """

    os.environ['DJANGO_SETTINGS_MODULE'] = 'authaction.test_settings'

    import django
    if django.VERSION >= (1, 7):
        # initialize the app regsitry
        django.setup()


def run_tests():

    setup()

    from django.conf import settings
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(
        ['authaction'],
    )

    sys.exit(failures)


if __name__ == '__main__':

    run_tests()
