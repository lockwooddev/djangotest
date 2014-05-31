from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from .utils import bubble_sort


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)

            if not self.user:
                raise forms.ValidationError(_('Invalid Login'))

        return self.cleaned_data


class NumberForm(forms.Form):
    numbers = forms.CharField(required=True)

    def clean_numbers(self):
        data = self.cleaned_data['numbers']

        sequence = data.split(',')
        new = []
        for item in sequence:
            try:
                number = float(item)
            except ValueError:
                continue

            # determine if input was an integer.
            str_float = str(number)
            decimal_value = str_float.split('.')[1]
            decimal_len = len(decimal_value)
            if decimal_len == 1 and decimal_value == '0':
                number = int(number)

            new.append(number)

        return bubble_sort(new)
