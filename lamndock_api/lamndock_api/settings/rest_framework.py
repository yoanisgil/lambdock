# -*- coding: utf-8 -*-

INSTALLED_APPS += (  # NOQA
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
)

REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100,
}

