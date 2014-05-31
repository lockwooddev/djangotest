import pytest

from dummy.apps.users.models import User


@pytest.mark.django_db
class TestUserModel:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user = User.objects.create_user(
            email='u@test.com',
            password='x',
            first_name='first',
            last_name='last')

    def test_get_full_name(self, client):
        full_name = self.user.get_full_name()
        assert full_name == u'{0} {1}'.format(self.user.first_name, self.user.last_name)

    def test_get_short_name(self, client):
        short_name = self.user.get_short_name()
        assert short_name == self.user.email

    def test_is_staff(self, client):
        assert not self.user.is_staff
