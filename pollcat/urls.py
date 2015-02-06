from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/complete/$',
        RedirectView.as_view(url="/"),
        name='registration_complete'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
