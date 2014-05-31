from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from dummy.apps.users.views import LoginView, LogoutView, NumbersView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(url=reverse_lazy('login')), name='logout'),
    url(r'^', NumbersView.as_view(), name='numbers'),
)

if settings.DEBUG and getattr(settings, 'MEDIA_FROM_TESTSERVER', False):
    urlpatterns += patterns('',
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )
