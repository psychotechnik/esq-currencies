from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

from django.contrib import admin

from django.contrib.comments.models import Comment
admin.site.unregister(Comment)

from django.contrib.sites.models import Site
admin.site.unregister(Site)

from django.contrib.flatpages.models import FlatPage
admin.site.unregister(FlatPage)

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
)
urlpatterns += patterns('',
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^', include(admin.site.urls)),

    #(r'^$', direct_to_template, { 'template': 'index.html' }),
    #(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/s/static/images/favicon.ico'}),
)

if getattr(settings, 'DEBUG', True):
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
