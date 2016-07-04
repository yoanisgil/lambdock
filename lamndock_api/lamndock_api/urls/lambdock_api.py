# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns

urlpatterns += patterns(  # NOQA
    '',
    url(r'^', include('functions.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
