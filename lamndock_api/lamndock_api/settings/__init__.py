# -*- coding: utf-8 -*-

import os

from split_settings.tools import optional, include

include(
    'base.py',
    'rest_framework.py',
    'lambdock_api.py',
    optional('local_settings.py'),
    scope=locals()
)

