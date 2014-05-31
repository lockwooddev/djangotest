from django.core.urlresolvers import reverse

from dummy.apps.users.models import User

import json
import pytest


@pytest.mark.django_db
class TestLoginLogoutView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user = User.objects.create_user(
            email='u@test.com', password='test', first_name='first', last_name='last')

    def test_get_success(self, client):
        response = client.get(reverse('login'))
        assert response.status_code == 200

    def test_login_with_existing_session(self, client):
        client.login(email=self.user.email, password='test')
        response = client.get(reverse('login'))
        assert response.status_code == 302

    def test_post_success(self, client):
        response = client.post(
            reverse('login'),
            data={
                'email': self.user.email,
                'password': 'test'
            }
        )
        assert response.status_code == 302
        assert self.user.id == client.session.get('_auth_user_id')

    def test_post_user_does_not_exist(self, client):
        response = client.post(
            reverse('login'),
            data={
                'email': 'another@test.com',
                'password': 'test'
            }
        )
        assert response.status_code == 200
        assert not response.context['form'].is_valid()
        assert len(response.context['form'].errors) == 1
        assert '__all__' in response.context['form'].errors
        assert not client.session

    def test_post_empty_fail(self, client):
        response = client.post(
            reverse('login'),
            data={
                'email': '',
                'password': ''
            }
        )
        assert response.status_code == 200
        assert not response.context['form'].is_valid()
        assert len(response.context['form'].errors) == 2
        assert 'password' in response.context['form'].errors
        assert 'email' in response.context['form'].errors
        assert not client.session

    def test_logout_no_session(self, client):
        response = client.get(reverse('logout'))
        assert response.status_code == 302
        assert not client.session.keys()

    def test_logout_with_session(self, client):
        # first login
        response = client.post(
            reverse('login'),
            data={
                'email': self.user.email,
                'password': 'test'
            }
        )
        assert response.status_code == 302
        assert self.user.id == client.session.get('_auth_user_id')

        # now logout
        response = client.get(reverse('logout'))
        assert response.status_code == 302
        assert not client.session.keys()


@pytest.mark.django_db
class TestNumbersView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user = User.objects.create_user(
            email='u@test.com', password='test', first_name='first', last_name='last')
        self.kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}

    def test_get_page_logged_in(self, client):
        client.login(email=self.user.email, password='test')
        response = client.get(reverse('numbers'))
        assert response.status_code == 200

    def test_get_page_not_logged_in(self, client):
        response = client.get(reverse('numbers'))
        assert response.status_code == 302

    def test_ajax_post_numbers(self, client):
        client.login(email=self.user.email, password='test')
        post_data = {"numbers": "10, 1, 1.4, -1"}
        response = client.post(reverse('numbers'), post_data, **self.kwargs)
        json_data = json.loads(response.content)
        assert len(json_data.keys()) == 1
        assert json_data['numbers'] == [-1, 1, 1.4, 10]
        assert response.status_code == 200

    def test_ajax_post_empty_numbers(self, client):
        client.login(email=self.user.email, password='test')
        post_data = {"numbers": ""}
        response = client.post(reverse('numbers'), post_data, **self.kwargs)
        json_data = json.loads(response.content)
        assert len(json_data.keys()) == 0
        assert response.status_code == 200
