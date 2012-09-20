from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytestsite.views.home', name='home'),
    # url(r'^mytestsite/', include('mytestsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^newscred/$', 'newscred.views.index'),
    url(r'^newscred/edit_topic/$', 'newscred.views.save_edited_topic'),
    url(r'^newscred/(?P<topic_id>\w+)/$', 'newscred.views.detail'),
)

urlpatterns += staticfiles_urlpatterns()
