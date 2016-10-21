from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello$', 'hello.views.home'),
    url(r'^$', 'hello.views.index'),
)
