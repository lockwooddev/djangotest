from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(_('email'), max_length=255, unique=True, db_index=True)
    first_name = models.CharField(_('first name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_admin = models.BooleanField(_('is admin'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
