from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from .forms import LoginForm, NumberForm

import json


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('numbers'))
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.user)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('numbers')


class LogoutView(RedirectView):

    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class NumbersView(FormView):

    form_class = NumberForm
    template_name = 'numbers.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NumbersView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.is_ajax():
            return HttpResponse(
                json.dumps(form.cleaned_data),
                status=200,
                content_type='application/json'
            )
        return super(NumbersView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return HttpResponse(
                json.dumps({}),
                status=200,
                content_type='application/json'
            )
        return super(NumbersView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('numbers')
