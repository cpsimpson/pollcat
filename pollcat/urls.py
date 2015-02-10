from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        login_form = AuthenticationForm()
        registration_form = RegistrationForm()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['login_form'] = login_form
        context['registration_form'] = registration_form
        return context


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/complete/$',
        RedirectView.as_view(url="/"),
        name='registration_complete'),
    url(r'^accounts/password/reset/complete/$',
        RedirectView.as_view(url="/"),
        name='auth_password_reset_complete'),
    (r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^polls/', include('ballots.polls_urls', namespace="polls")),
    url(r'^ballots/', include('ballots.urls', namespace="ballots")),
)
