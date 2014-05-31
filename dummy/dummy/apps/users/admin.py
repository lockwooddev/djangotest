from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext as _

from .models import User


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active']

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = (
        'email', 'first_name', 'last_name', 'is_active', 'date_joined')

    fieldsets = (
        (_('Required'), {'fields': ('email', 'password')}),
        (_('General'), {
            'fields': ('first_name', 'last_name', 'date_joined')}),
        (_('Status'), {
            'fields': (
                'is_active', 'is_admin',
            )
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(UserAdmin, self).get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(UserAdmin, self).get_form(request, obj, **defaults)

    def lookup_allowed(self, lookup, value):
        # See #20078: we don't want to allow any lookups involving passwords.
        if lookup.startswith('password'):
            return False
        return super(UserAdmin, self).lookup_allowed(lookup, value)


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
