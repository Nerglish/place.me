from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'placeme.views.index', name='index'),

    # JSON urls
    url(r'^api)/$', 'placeme.views.query', name='query'),
)
