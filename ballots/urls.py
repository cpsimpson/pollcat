from django.conf.urls import patterns, include, url
from ballots import views


urlpatterns = patterns('',
    # url(r'^$', views.BallotIndexView.as_view(), name='index'),
    # url(r'^(?P<slug>\w+)/$', views.BallotDetailView.as_view(), name='detail'),
    # url(r'^(?P<slug>\w+)/results/$', views.BallotResultsView.as_view(), name='results'),
)
