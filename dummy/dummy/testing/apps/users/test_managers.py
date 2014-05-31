from django.db import IntegrityError

from dummy.apps.users.models import User

import pytest


@pytest.mark.django_db
class TestUserManager:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.email = 'u@test.com'
        self.first_name = 'Amos'
        self.last_name = 'Elon'

    def test_create_user(self, client):
        ''' Tests succesfull user creation '''
        user = User.objects.create_user(
            email=self.email, password='x', first_name=self.first_name, last_name=self.last_name)
        assert User.objects.count() == 1
        assert user.email == self.email
        assert not user.is_admin
        assert user.first_name == self.first_name
        assert user.last_name == self.last_name
        assert user.date_joined

    def test_create_superuser(self, client):
        ''' Tests succesfull superuser creation '''
        user = User.objects.create_superuser(
            email=self.email, password='x', first_name=self.first_name, last_name=self.last_name)
        assert User.objects.count() == 1
        assert user.email == self.email
        assert user.is_admin
        assert user.first_name == self.first_name
        assert user.last_name == self.last_name
        assert user.date_joined

    def test_create_user_with_missing_email(self, client):
        ''' Tests failed user creation on missing fields '''
        with pytest.raises(IntegrityError):
            User.objects.create_user(email=None, password='x')
