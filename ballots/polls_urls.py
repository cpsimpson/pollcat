from django.conf.urls import patterns, include, url
from ballots import views


urlpatterns = patterns('',
    url(r'^$', views.PollIndexView.as_view(), name='index'),
    url(r'^(?P<slug>\w+)/$', views.PollDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>\w+)/results/$', views.PollResultsView.as_view(), name='results'),
    url(r'^(?P<slug>\w+)/vote/$', views.vote, name='vote'),
)