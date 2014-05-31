from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_admin, **extra_fields):
        now = timezone.now()

        new_user = self.model(
            email=email,
            is_active=True,
            is_admin=is_admin,
            last_login=now,
            **extra_fields
        )

        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)
