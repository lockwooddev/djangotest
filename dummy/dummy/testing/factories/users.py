import factory
from dummy.apps.users.models import User


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    first_name = factory.Sequence(lambda n: 'First {}'.format(n))
    last_name = factory.Sequence(lambda n: 'Last {}'.format(n))
