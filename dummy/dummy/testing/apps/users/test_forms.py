import pytest

from dummy.apps.users.forms import LoginForm, NumberForm
from dummy.apps.users.models import User


@pytest.mark.django_db
class TestLoginForm:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.form = LoginForm
        self.user = User.objects.create_user(
            email='u@test.com',
            password='testpassword',
            first_name='first',
            last_name='last')

    def test_form_valid(self, client):
        form = self.form({
            'email': self.user.email,
            'password': 'testpassword',
        })
        valid = form.is_valid()
        assert valid
        assert form.user == self.user

    def test_form_missing_required(self, client):
        form = self.form({
            'email': '',
            'password': '',
        })
        assert not form.is_valid()
        assert len(form.errors) == 2
        assert 'email' in form.errors
        assert 'password' in form.errors
        assert not form.user

    def test_form_invalid_email(self, client):
        form = self.form({
            'email': 'test',
            'password': 'testpassword',
        })
        assert not form.is_valid()
        assert len(form.errors) == 1
        assert 'email' in form.errors
        assert 'password' not in form.errors
        assert not form.user


class TestNumberForm:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.form = NumberForm

    def test_valid_numbers(self, client):
        form = self.form({
            'numbers': "$, -1.15, 2, 3, 1, -100, abc"
        })

        assert form.is_valid()
        assert form.cleaned_data['numbers'] == [-100, -1.15, 1, 2, 3]

    def test_empty_numbers(self, client):
        form = self.form({})
        assert not form.is_valid()
        assert len(form.errors) == 1
        assert 'numbers' in form.errors
