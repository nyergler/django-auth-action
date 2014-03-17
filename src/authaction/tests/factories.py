import factory

from django.contrib.auth import models as auth_models


class UserFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = auth_models.User

    username = factory.Sequence(
        lambda n: 'user{0}'.format(n),
    )
    email = factory.Sequence(
        lambda n: 'user_{0}@example.com'.format(n),
    )
    password = factory.PostGenerationMethodCall(
        'set_password',
        'blarf',
    )
